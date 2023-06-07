from rest_framework import serializers


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField()
