from django.urls import path
from . import views

app_name = 'chat'
urlpatterns = [
    path('catchat/<int:pk>', views.ChatViewCaterer.as_view(), name='chat_caterer'),
    path('conchat/<int:pk>', views.ChatViewConsumer.as_view(), name='chat_consumer'),
    path('catchat/<int:pk>/<int:consumer_id>', views.ChatViewCatererSpecific.as_view(), name='chat_caterer_specific'),
]
