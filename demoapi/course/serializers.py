from rest_framework import serializers
from .models import Course


class GetAllCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'price', 'content',)


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    price1 = serializers.IntegerField()
    content2 = serializers.CharField(max_length=200)
