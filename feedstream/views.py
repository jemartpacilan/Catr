from django.views import View
from django.views.generic import DetailView, ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Avg
from django.db import transaction
# Create your views here.

from registration.models import Caterer, Consumer
from review.models import Review, Question, Answer
from registration.forms import UserLoginForm,\
    UserSignUpForm,\
    CatererSignUpForm,\
    ConsumerSignUpForm\


# To handle the main feedstream


class IndexView(ListView):
    model = Caterer
    login_url = '/registration/login'
    template_name = 'feedstream/index.html'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data['user_login_form'] = UserLoginForm()
        data['user_signup_form'] = UserSignUpForm()
        data['caterer_signup_form'] = CatererSignUpForm()
        data['consumer_signup_form'] = ConsumerSignUpForm()
        data['all_caterer_objects'] = Caterer.objects.all()

        return data


# To handle the about page view
class AboutView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request):
        return render(request, 'feedstream/about.html')


# To handle ordering given caterer instance
class OrderView(DetailView):
    # login_url = '/registration/login'
    model = Caterer
    template_name = 'feedstream/order.html'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        caterer_id = self.kwargs['pk']

        all_reviews = Review.objects.filter(
            caterer_id=caterer_id).order_by('review_date_submitted')

        review_average = Caterer.objects\
                                .filter(id=caterer_id)\
                                .annotate(
                                    avg_rating=Avg('review__review_rating'))\
                                .first().avg_rating\
            if all_reviews.exists() else 0

        data['reviews'] = all_reviews

        try:
            data['user_type'] = self.request.user.catruser.user_type
        except(KeyError, AttributeError):
            data['user_type'] = None

        data['questions'] = Question.objects\
                                    .filter(caterer_id=caterer_id)\
                                    .order_by('question_date_submitted')

        data['average'] = review_average

        data['answers'] = Answer.objects\
                                .filter(caterer_id=caterer_id)\
                                .order_by('answer_date_submitted')

        data['caterer'] = get_object_or_404(Caterer, pk=caterer_id)

        try:
            data['consumer'] = Consumer.objects.get(
                pk=self.request.user.catruser.id)
        except(KeyError, Consumer.DoesNotExist, AttributeError):
            data['consumer'] = None

        return data

# To handle ordering given caterer instance


class PaymentView(LoginRequiredMixin, View):
    login_url = '/registration/login'

    def get(self, request):
        return render(request, 'feedstream/payment.html')


# returns an array of caterers plus their review average
class TotalRatingView(View):
    # login_url = '/registration/login'

    def get(self, request):
        context = []
        catererList = Caterer.objects.all()
        for caterer in catererList:
            lowest = 0
            highest = 0
            prices = []

            print(caterer.business_name)
            for menu in caterer.menu_set.all():
                print(menu.package.package_name)
                if menu.package.package_name != 'No package':
                    sum = 0
                    for item in menu.package.menu_set.all():
                        sum += item.course.course_price
                        # print(sum)
                    prices.append(sum)

            sum = 0
            for review in caterer.review_set.all():
                sum += review.review_rating
            count = caterer.review_set.all().count()
            if count == 0:
                average = 0
            else:
                average = sum / count
            # print(caterer.profile_image.url)
            if not prices:
                lowest = highest = 0
            else:
                prices = sorted(prices, key=int)
                lowest = prices[0]
                highest = prices[len(prices) - 1]

            context.append({
                'caterer': caterer.asdict(),
                'average': average,
                'lowest': lowest,
                'highest': highest,
                'distance': None}),

        return JsonResponse({'caterers_data': context})
