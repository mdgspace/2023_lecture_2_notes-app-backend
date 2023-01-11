from urllib.request import Request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404, JsonResponse
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import User
from rest_framework.parsers import JSONParser


class UserSiginView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        username = data['username']
        password = data['password']
        try:
            user = User.objects.get(username=username)
            user_data = UserSerializer(user).data
            if(user_data['password'] == password):
                return Response(username,status=201)
            return Response('Invalid Credentials', status=400)
        except User.DoesNotExist:
            return Response('Invalid Credentials', status=400)
        
        

class UserSignupView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if(serializer.is_valid()): 
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)