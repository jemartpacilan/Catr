from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

from registration.models import Caterer, Consumer, Transaction
from orders.models import Tray
from .models import CreditCardTransaction,\
    PayPalTransaction

from .forms import CashPaymentForm,\
    PaypalPaymentForm,\
    CreditCardPaymentForm

import datetime

# To handle the payment page view
class PaymentView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    @transaction.atomic
    def get(self, request, **kwargs):
        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)

        data = {}
        caterer_id = self.kwargs['pk']

        transaction = None
        tray = None

        try:
            transaction = consumer.history.transaction_set\
                                  .exclude(tray__exact=None)\
                                  .get(caterer_id=caterer_id)
        except (KeyError, Transaction.DoesNotExist):
            return redirect(reverse('orders:book', args=(caterer_id,)))

        tray = transaction.tray

        data['tray'] = tray
        data['item_set'] = tray.item_set.all() if type(tray) is Tray else []
        data['current_user'] = consumer
        data['caterer'] = get_object_or_404(Caterer, pk=caterer_id)
        data['cash_payment_form'] = CashPaymentForm()
        data['paypal_payment_form'] = PaypalPaymentForm()
        data['credit_card_payment_form'] = CreditCardPaymentForm()

        return render(request, 'payment/payment.html', data)

    @transaction.atomic
    def post(self, request, pk):
        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)

        caterer = get_object_or_404(Caterer,
                                    pk=pk)
        try:
            transaction = consumer.history.transaction_set\
                                  .exclude(tray__exact=None)\
                                  .get(caterer_id=pk)
        except (KeyError, Transaction.DoesNotExist):
            return redirect(reverse('orders:book', args=(pk, )))

        if 'PayPal_username' in request.POST:
            pp_trans = PayPalTransaction(
                caterer=caterer,
                holder=consumer,
                paypal_username=request.POST['PayPal_username']
            )
            pp_trans.save()
        elif 'cvv' in request.POST:
            expiration_date_string = '{}{}{}'.format(
                request.POST['expiration_date_day'],
                request.POST['expiration_date_month'],
                request.POST['expiration_date_year']
            )

            expiration_date = datetime.datetime.strptime(
                expiration_date_string,
                '%d%m%Y'
            ).date()
            cc_trans = CreditCardTransaction(
                caterer=caterer,
                consumer=consumer,
                expiration_date=expiration_date,
                card_number=request.POST['card_number'],
                card_holder=request.POST['name_on_card'],
                cvv=request.POST['cvv']
            )
            cc_trans.save()

        transaction.transaction_event_street_location = request.POST['street']
        transaction.transaction_event_building_location = request.POST['building_number']
        transaction.transaction_event_unit_number = request.POST['unit_number']
        transaction.transction_other_instructions = request.POST['other_instructions']

        transaction.save()

        return redirect(reverse('payment:payment', args=(pk, )))
