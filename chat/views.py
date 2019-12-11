from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

# Create your views here.

from registration.models import Caterer, Consumer
from chat.models import Message


# To handle the payment page view
class ChatViewCaterer(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    @transaction.atomic
    def get(self, request, pk):
        context = {
            'consumers': Consumer.objects.all(),
            'caterer': get_object_or_404(Caterer, pk=pk)
        }
        return render(request, 'chat/chat_caterer.html', context)


class ChatViewCatererSpecific(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    @transaction.atomic
    def get(self, request, pk, consumer_id):
        consumer = Consumer.objects.get(pk=consumer_id)
        messages = consumer.message_set.order_by('message_date_submitted')\
                                       .filter(caterer_id=pk)
        caterer = Caterer.objects.get(pk=pk)

        context = {
            'consumers': Consumer.objects.all(),
            'consumer': consumer,
            'messages': messages,
            'caterer': caterer,
        }
        return render(request, 'chat/chat_caterer.html', context)

    @transaction.atomic
    def post(self, request, pk, consumer_id):
        message = Message()
        message.message_body = request.POST['msgTxt']
        message.caterer = Caterer.objects.get(pk=pk)
        message.consumer = Consumer.objects.get(pk=consumer_id)
        message.message_owned_by_consumer = False
        message.save()

        consumer = Consumer.objects.get(pk=consumer_id)
        messages = consumer.message_set.order_by('message_date_submitted')\
                                       .filter(caterer_id=pk)
        caterer = Caterer.objects.get(pk=pk)

        context = {
            'consumers': Consumer.objects.all(),
            'consumer': consumer,
            'messages': messages,
            'caterer': caterer,
        }

        return render(request, 'chat/chat_caterer.html', context)


class ChatViewConsumer(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    @transaction.atomic
    def get(self, request, pk):
        consumer = Consumer.objects.get(pk=request.user.catruser.id)
        messages = consumer.message_set.order_by('message_date_submitted')\
                                       .filter(caterer_id=pk)
        caterer = Caterer.objects.get(pk=pk)

        context = {
            'consumer': consumer,
            'messages': messages,
            'caterer': caterer,
        }
        return render(request, 'chat/chat_consumer.html', context)

    @transaction.atomic
    def post(self, request, pk):
        message = Message()
        message.message_body = request.POST['msgTxt']
        message.caterer = Caterer.objects.get(pk=pk)
        message.consumer = Consumer.objects.get(pk=request.user.catruser.id)
        message.message_owned_by_consumer = True
        message.save()

        consumer = Consumer.objects.get(pk=request.user.catruser.id)
        messages = consumer.message_set.order_by('message_date_submitted')\
                                       .filter(caterer_id=pk)
        caterer = Caterer.objects.get(pk=pk)

        context = {
            'consumer': consumer,
            'messages': messages,
            'caterer': caterer,
        }

        return render(request, 'chat/chat_consumer.html', context)
