from django.db import models
from django.utils import timezone

from registration.models import Caterer, Consumer
# Create your models here.


class Review(models.Model):
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    review_body = models.CharField(max_length=1000)
    review_rating = models.IntegerField()
    review_date_submitted = models.DateTimeField('date submitted',
                                                 editable=False)
    review_date_modified = models.DateTimeField()

    def __str__(self):
        return "{}  x  {}---- Rating: {}".format(self.caterer,
                                                 self.consumer,
                                                 self.review_rating)

    def save(self, *args, **kwargs):
        self.review_date_modified = timezone.now()
        if self.review_date_submitted is None:
            self.review_date_submitted = timezone.now()
        return super(Review, self).save(*args, **kwargs)


class Question(models.Model):
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    question_body = models.CharField(max_length=1000)
    question_date_submitted = models.DateTimeField('date submited',
                                                   editable=False)

    def __str__(self):
        return "Question by: {} on {}".format(self.consumer,
                                              self.question_date_submitted)

    def save(self, *args, **kwargs):
        if self.question_date_submitted is None:
            self.question_date_submitted = timezone.now()
        return super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)

    answer_body = models.CharField(max_length=1000)
    answer_date_submitted = models.DateTimeField('date submited',
                                                 editable=False)

    def __str__(self):
        return "Answer by: {} on {}".format(self.caterer,
                                            self.answer_date_submitted)

    def save(self, *args, **kwargs):
        if self.answer_date_submitted is None:
            self.answer_date_submitted = timezone.now()
        return super(Answer, self).save(*args, **kwargs)
