from django.urls import path
from .api_views import SendMessage


urlpatterns = [
    path("send", SendMessage.as_view(), name="send"),
]