from django.urls import path
from .import views

app_name = 'orders'
urlpatterns = [
    path('book/<int:pk>/', views.BookView.as_view(), name='book'),
    path('ajax/remove/<int:pk>/', views.RemoveCourseView.as_view(),
         name='remove_course'),

    # the following views return JSON responses

    path('ajax/search/<int:pk>/', views.SearchCourseView.as_view(),
         name='search_course'),
    path('ajax/add/<int:pk>/', views.AddCourseView.as_view(),
         name='add_course'),
    path('ajax/retrieveCourse/<int:pk>/', views.RetrieveCourseView.as_view(),
         name='retrieve_course'),
]
