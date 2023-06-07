from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import InfoSerializer
from rest_framework import permissions



# Create your views here.
class TestAPI(APIView):
    def get(self, request):
        return Response('oke')
    
    def post(self, request):
        data = InfoSerializer(data=request.data)
        print(data)
        if not data.is_valid():
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data.data, status=status.HTTP_200_OK)
    
class NotAuthen(APIView):
    permissions_classes = (permissions.AllowAny,)
    def get(self, request):
        return Response('not authen')