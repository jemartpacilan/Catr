from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.views import generic
from django.db import transaction
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone

from registration.forms import UserLoginForm, UserSignUpForm,\
    CatererSignUpForm, ConsumerSignUpForm

from orders.models import History
from .models import Consumer
import logging

logger = logging.getLogger(__name__)


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = UserLoginForm
    success_url = '/thanks/'

    def form_valid(self, form):
        return redirect(reverse('feedstream:index'))

    @transaction.atomic
    def post(self, request):
        username = request.POST['username']
        raw_password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=raw_password
        )

        if user is not None:
            login(request, user)
            return redirect(reverse('feedstream:index'))
        else:
            return render(request, 'registration/login.html')


class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return render(request, 'registration/logout_success.html')


class CatererSignUpView(FormView):
    template_name = 'registration/catsignup.html'
    success_url = '/feedstream/'

    @transaction.atomic
    def post(self, request):
        user_signup_form = UserSignUpForm(request.POST)
        caterer_signup_form = CatererSignUpForm(request.POST, request.FILES)

        if user_signup_form.is_valid() and caterer_signup_form.is_valid():
            # change these names to actual names used in template
            new_user = user_signup_form.save()
            new_user.save()

            caterer_signup_form = CatererSignUpForm(
                request.POST, request.FILES
            )
            new_caterer = caterer_signup_form.save(commit=False)

            new_caterer.first_name = request.POST['first_name']
            new_caterer.last_name = request.POST['last_name']
            new_caterer.email = request.POST['email']
            new_caterer.user_type = 0
            new_caterer.user_id = new_user.id
            new_caterer.save()

            user_to_authenticate = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password1']
            )            

            user_to_authenticate.save()
            login(request, user_to_authenticate)
            # change to appropriate signup success url
            return redirect(reverse('feedstream:index'))
        else:
            user_signup_form = UserSignUpForm(
                request.POST or None,
                request.FILES or None,
            )
            caterer_signup_form = CatererSignUpForm(
                request.POST or None,
                request.FILES or None
            )

            messages.error(request, "Error")

        return render(
            request,
            'registration/catsignup.html',
            {
                'caterer_signup_form': caterer_signup_form,
                'user_signup_form': user_signup_form
            }
        )

    def get(self, request):
        caterer_signup_form = CatererSignUpForm()
        user_signup_form = UserSignUpForm()

        return render(
            request,
            'registration/catsignup.html',
            {
                'caterer_signup_form': caterer_signup_form,
                'user_signup_form': user_signup_form
            }
        )


class ConsumerSignUpView(FormView):
    template_name = 'registration/consignup.html'
    form_class = ConsumerSignUpForm
    success_url = '/feedstream/'

    @transaction.atomic
    def post(self, request):
        user_signup_form = UserSignUpForm(request.POST)
        consumer_signup_form = ConsumerSignUpForm(request.POST, request.FILES)

        if user_signup_form.is_valid() and consumer_signup_form.is_valid():
            new_user = user_signup_form.save()
            new_user.save()
            # change these names to actual names used in template

            new_consumer = consumer_signup_form.save(commit=False)

            new_consumer.first_name = request.POST['first_name']
            new_consumer.last_name = request.POST['last_name']
            new_consumer.email = request.POST['email']
            new_consumer.user_id = new_user.id
            new_consumer.user_type = 1

            history = History(history_points=0)
            history.save()

            new_consumer.history = history
            new_consumer.consumer_badge = 0

            new_consumer.save()

            user_to_authenticate = authenticate(
                request,
                username=request.POST['username'],
                password=request.POST['password1']
            )

            login(request, user_to_authenticate)
            # change to appropriate signup success url
            return redirect(reverse('feedstream:index'))
        else:
            form = ConsumerSignUpForm(request.POST or None,
                                      request.FILES or None)
        return render(request, 'registration/consignup.html',
                      {'consumer_signup_form': form})

    def get(self, request):
        form = ConsumerSignUpForm()
        return render(request, 'registration/consignup.html',
                      {'consumer_signup_form': form})
