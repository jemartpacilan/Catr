from django.urls import path
from .import views

app_name = 'payment'
urlpatterns = [
    path('<int:pk>', views.PaymentView.as_view(), name='payment'),
]
