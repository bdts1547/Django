from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from rfApp.serializers import StudentSerializer
from rfApp.models import Student


class TestView(APIView):
    def get(self, request):
        
        permission_classes = (IsAuthenticated, )

        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

