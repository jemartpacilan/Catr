from rest_framework import viewsets
from .models import Course, Tray, History
from .serializer import CourseSerializer,\
    TraySerializer,\
    HistorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class TrayViewSet(viewsets.ModelViewSet):
    queryset = Tray.objects.all()
    serializer_class = TraySerializer


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
