from django.urls import path
from . import views

app_name = 'registration'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('catsignup/', views.CatererSignUpView.as_view(), name='catsignup'),
    path('consignup/', views.ConsumerSignUpView.as_view(), name='consignup'),
]
