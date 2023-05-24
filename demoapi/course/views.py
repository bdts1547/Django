from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer



# Create your views here.
class GetAllCourseAPIView(APIView):
    def get(self, request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print("POST")
        myData = CourseSerializer(data=request.data)
        if myData.is_valid():
            title = myData.data['title']
            price = myData.data['price1']
            content = myData.data['content2']
            course = Course.objects.create(title=title, price=price, content=content)
            return Response(course.title, status.HTTP_200_OK)
        else:
            return Response("Invalid data", status.HTTP_400_BAD_REQUEST)