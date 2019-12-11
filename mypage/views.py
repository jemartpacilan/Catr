from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.db import transaction

from registration.models import Caterer, Consumer, Image, Menu, Package
from orders.models import Course
# Create your views here.


# To handle the payment page view
class ConsumerPageView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    def get(self, request, pk):
        consumer = get_object_or_404(Consumer, pk=pk)
        context = {'consumer': consumer}
        return render(request, 'profile_consumer.html', context)


class EditConsumerPageView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    def get(self, request, pk):
        consumer = get_object_or_404(Consumer, pk=pk)
        context = {'consumer': consumer}
        return render(request, 'editprofile_consumer.html', context)

    @transaction.atomic
    def post(self, request, pk):
        if request.POST['password1'] == request.POST['password2']:
            consumer = get_object_or_404(Consumer, pk=pk)
            consumer.first_name = request.POST['fName']
            consumer.last_name = request.POST['lName']
            consumer.email = request.POST['email']
            consumer.user.password = request.POST['password1']
            consumer.user.save()
            consumer.save()
            login(request, consumer.user)
            if request.FILES:
                consumer.profile_image = request.FILES['profile_image']
            consumer.save()
        else:
            return redirect(reverse('mypage:editprofile_consumer', args=(pk,)))
        return redirect(reverse('mypage:editprofile_consumer', args=(pk,)))


class CatererPageView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    def get(self, request, pk):
        caterer = get_object_or_404(Caterer, pk=request.user.catruser.id)
        packages = Package.objects.filter(caterer_id__exact=caterer.id)
        images = Image.objects.filter(menu__caterer_id__exact=caterer.id)
        context = {
            'caterer': caterer,
            'packages': packages,
            'images': images,
        }
        return render(request, 'profile_caterer.html', context)


class EditCatererPageView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    def get(self, request, pk):
        caterer = get_object_or_404(Caterer, pk=pk)
        context = {'caterer': caterer}
        return render(request, 'editprofile_caterer.html', context)

    @transaction.atomic
    def post(self, request, pk):
        print(request.FILES)
        if not request.FILES:
            caterer = get_object_or_404(Caterer, pk=pk)
            caterer.business_name = request.POST['bname']
            caterer.municipality_address = request.POST['municipality']
            caterer.street_address = request.POST['street']
            caterer.zip_code = request.POST['zip']
            caterer.business_description = request.POST['bDescription']
            caterer.save()
        else:
            caterer = get_object_or_404(Caterer, pk=pk)
            caterer.profile_image = request.FILES['profile']
            caterer.save()
        return redirect(reverse('mypage:profile_caterer', args=(pk,)))


class AddMenuView(LoginRequiredMixin, DetailView):
    login_url = '/registration/login'

    def get(self, request, pk):
        caterer = Caterer.objects.get(pk=pk)
        packages = Package.objects.filter(caterer=caterer)
        context = {
            'caterer': caterer,
            'packages': packages,
        }
        return render(request, 'addmenu.html', context)

    def post(self, request, pk):
        caterer = get_object_or_404(Caterer, pk=pk)
        course = Course(
            course_name=request.POST['cname'],
            course_description=request.POST['cdescription'],
            course_category=request.POST['ccategory'],
            course_unit=request.POST['cunit'],
            course_price=request.POST['cprice']
        )
        course.save()

        menu = Menu(
            course=course,
            caterer=caterer,
            package=Package.objects.get(pk=request.POST['packages']),
        )

        menu.save()

        context = {
            'caterer': caterer,
            'packages': Package.objects.filter(caterer=caterer)
        }

        return render(request, 'addmenu.html', context)

