from django.urls import path
from .views import SendMessage, ReceiveMessage

urlpatterns = [
    path('send', SendMessage.as_view(), name='send_message'),
    path('receive', ReceiveMessage.as_view(), name='receive_message')
]
