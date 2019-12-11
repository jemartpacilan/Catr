from rest_framework import serializers
from .models import Course, Tray, History


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class TraySerializer(serializers.ModelSerializer):
    class Meta:
        model = Tray
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
