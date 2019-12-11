from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.urls import reverse
from django.db import transaction
from django.db.models import Avg
from django.views.generic import DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import *

from registration.models import Caterer, Consumer, Menu, Item, Transaction
from orders.models import Tray
from review.models import Review
from django.http import JsonResponse

import logging
import re

# create logger for exporting details in a file
logger = logging.getLogger(__name__)


class BookView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'
    model = Caterer
    template_name = 'orders/book.html'
    caterer = 'all_caterer_objects'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        caterer_id = self.kwargs['pk']

        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)
        caterer = get_object_or_404(Caterer, pk=caterer_id)

        all_reviews = Review.objects.filter(
            caterer_id=caterer_id).order_by('review_date_submitted')

        review_average = Caterer.objects\
                                .filter(id=caterer_id)\
                                .annotate(
                                    avg_rating=Avg('review__review_rating'))\
                                .first().avg_rating\
            if all_reviews.exists() else 0

        transaction = None
        tray = None

        try:
            transaction = consumer.history.transaction_set\
                                  .exclude(tray__exact=None)\
                                  .get(caterer_id=caterer_id)
        except (KeyError, Transaction.DoesNotExist):
            data['tray'] = None

        if transaction is not None:
            tray = transaction.tray

        packages_set = [package
                        for package in caterer.package_set.all()]

        data['menu'] = Menu.objects.filter(caterer_id=caterer_id)
        data['consumer'] = consumer
        data['packages'] = packages_set
        data['average'] = review_average
        data['item_set'] = tray.item_set.all() if type(tray) is Tray else []

        return data

    @transaction.atomic
    def post(self, request, pk):
        caterer = get_object_or_404(Caterer, pk=pk)
        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)

        try:
            transaction = consumer.history.transaction_set\
                                  .exclude(tray__exact=None)\
                                  .get(caterer_id=caterer.id)

        except (KeyError, Transaction.DoesNotExist):
            transaction = Transaction(transaction_date=timezone.now())
            tray = Tray(tray_cumulative_price=0, created_date=timezone.now())
            tray.save()
            transaction.transaction_is_completed = False
            transaction.tray = tray
            transaction.history = consumer.history
            transaction.caterer = caterer
            transaction.save()

        tray = transaction.tray

        # find the key that matches an integer, which should be the menu_id

        for key in request.POST:
            if re.match("^[0-9]+$", key):
                try:
                    menu_id = int(key)
                    queried_menu_item = get_object_or_404(Menu, pk=menu_id)
                    pass

                except (KeyError, Menu):
                    return render(request, 'orders/book.html', {
                        'menu': Menu.objects.filter(caterer_id=caterer.id),
                        'packages': [menu.package for menu
                                     in caterer.menu_set.distinct('package')],
                        'item_set': tray.item_set.all(),
                        'tray': tray
                    })

                else:
                    item = Item()
                    item.menu = queried_menu_item
                    tray.tray_cumulative_price += Decimal(
                        request.POST[key + 'x'])
                    tray.save()
                    item.tray = tray
                    item.item_quantity = request.POST[key + 'z']
                    # logger.error(tray)
                    # logger.error(item.tray)
                    item.save()
                    # logger.error(item.tray.tray_cumulative_price)

        return redirect(
            reverse('orders:book', args=(pk,)))


# used to return a json response filled with course data from a request
class SearchCourseView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request, pk):
        caterer = get_object_or_404(Caterer, pk=pk)
        data = caterer.menu_set.all()
        context = list(set([(x.id, x.course.course_name) for x in data]))
        return JsonResponse({'courses': context})


# removes a course given a pk
class RemoveCourseView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request, pk):
        itemtoremove = request.GET.get('item')
        c = get_object_or_404(Consumer, pk=request.user.catruser.id)
        alltrans = c.history.transaction_set.all()

        for t in alltrans:
            if len(t.tray.item_set.all()) > 0:
                item = t.tray.item_set.filter(
                    menu__caterer__id=pk,
                    menu__course__course_name=itemtoremove)

                for i in item:
                    logger.error('tae hehehe')
                    logger.error(i.menu.course.course_price)
                    new_price = i.tray.tray_cumulative_price - (i.menu.course.course_price * i.item_quantity)
                    logger.error(new_price)
                    # tray = Tray.objects.get(pk= i.tray.id)
                    t.tray.tray_cumulative_price = new_price
                    t.tray.save()
                    logger.error('asdgfsadgf')
                    logger.error(t.tray.tray_cumulative_price)
                    # logger.error(i.tray.id)
                    # tray.update(
                        # tray_cumulative_price=new_price)

                item.delete()

                logger.error(t.tray.item_set.all())
                if len(t.tray.item_set.all()) == 0:
                    t.tray.delete()

        return redirect(reverse('orders:book', args=(pk,)))


# return a course to add to a Tray object
class AddCourseView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request, pk):
        itemtoadd = request.GET.get('item')
        caterer = get_object_or_404(Caterer, pk=pk)
        data = caterer.menu_set.filter(course__course_name=itemtoadd).first()
        context = [(data.id, data.course.course_name)]
        return JsonResponse({'course': context})


# get course price
class RetrieveCourseView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request, pk):
        itemtoget = request.GET.get('name')
        caterer = get_object_or_404(Caterer, pk=pk)
        data = caterer.menu_set.filter(course__course_name=itemtoget).first()
        context = [(data.course.course_price)]
        return JsonResponse({'price': context})
