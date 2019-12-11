from django.urls import path
from .import views

app_name = 'mypage'
urlpatterns = [
    path('profile_consumer/<int:pk>',
         views.ConsumerPageView.as_view(),
         name='profile_consumer'),
    path('profile_consumer/<int:pk>/edit',
         views.EditConsumerPageView.as_view(),
         name='editprofile_consumer'),
    path('profile_caterer/<int:pk>',
         views.CatererPageView.as_view(),
         name='profile_caterer'),
    path('profile_caterer/<int:pk>/edit',
         views.EditCatererPageView.as_view(),
         name='editprofile_caterer'),
    path('profile_caterer/<int:pk>/addmenu',
         views.AddMenuView.as_view(),
         name='addmenu'),

]
