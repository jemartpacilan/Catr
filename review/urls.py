from django.urls import path

# TODO input paths here, if any

from . import views

app_name = 'review'
urlpatterns = [
    path('review/addreview', views.ReviewView.as_view(), name='addreview'),
    path('review/addquestion', views.QuestionView.as_view(),
         name='addquestion'),
    path('review/addanswer', views.AnswerView.as_view(),
         name='addanswer')
]
