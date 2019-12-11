from django.views import View
from django.urls import reverse
from django.db import transaction
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review, Question, Answer
from registration.models import Caterer, Consumer

# Create your views here.


class ReviewView(LoginRequiredMixin, View):
    login_url = 'registration/login'

    @transaction.atomic
    def post(self, request):
        review = Review()
        pk = int(request.POST['caterer'])

        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)
        caterer = get_object_or_404(Caterer, pk=int(request.POST['caterer']))
        review_body = request.POST['review-body']
        review_rating = request.POST['review-rating']

        review.consumer = consumer
        review.caterer = caterer
        review.review_body = review_body
        review.review_rating = review_rating

        review.save()
        return redirect(
            reverse('feedstream:order', args=(pk,)))


class QuestionView(LoginRequiredMixin, View):
    login_url = 'registration/login'

    @transaction.atomic
    def post(self, request):
        question = Question()

        pk = int(request.POST['caterer'])
        consumer = get_object_or_404(Consumer,
                                     pk=self.request.user.catruser.id)
        caterer = get_object_or_404(Caterer, pk=pk)
        question_body = request.POST['question-body']

        question.consumer = consumer
        question.caterer = caterer
        question.question_body = question_body

        question.save()
        return redirect(
            reverse('feedstream:order', args=(pk,)))


class AnswerView(LoginRequiredMixin, View):
    login_url = 'registration/login'

    @transaction.atomic
    def post(self, request):
        answer = Answer()

        pk = int(request.POST['caterer'])
        question = get_object_or_404(Question,
                                     pk=int(request.POST['question']))
        caterer = get_object_or_404(Caterer,
                                    pk=pk)
        answer_body = request.POST['answer-body']

        answer.question = question
        answer.caterer = caterer
        answer.answer_body = answer_body

        answer.save()
        return redirect(
            reverse('feedstream:order', args=(pk,)))
