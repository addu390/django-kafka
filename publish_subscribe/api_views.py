from rest_framework.views import APIView
from .models import MessageSerializer, Message
from rest_framework.response import Response
from .producers import send


class SendMessage(APIView):

    def post(self, request):
        username = request.data.get("username"),
        data = request.data.get("data")

        message = Message.objects.create(username=username, data=data)
        send(message)

        return Response({"success": True})
