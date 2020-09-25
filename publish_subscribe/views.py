from rest_framework.views import APIView
from .producers import send
from rest_framework.response import Response
from rest_framework import status
from .consumer import receive


class SendMessage(APIView):

    def post(self, request):
        username = request.data.get("username")
        token = request.data.get("token")
        data = request.data.get("data")

        send(username, data, token)

        return Response({"success": True}, status=status.HTTP_201_CREATED)


class ReceiveMessage(APIView):

    def post(self, request):
        receive()

        return Response({"success": True}, status=status.HTTP_201_CREATED)
