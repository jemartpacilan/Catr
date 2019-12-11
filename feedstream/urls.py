from django.urls import path
from . import views

app_name = 'feedstream'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.OrderView.as_view(), name='order'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('ajax/reviewtotal/', views.TotalRatingView.as_view(),
         name='total_review'),
]
