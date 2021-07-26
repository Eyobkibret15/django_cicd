from django.shortcuts import render
from .models import student
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from .serializers import claser

# Create your views here
from rest_framework.viewsets import ModelViewSet


class students(ModelViewSet):
    serializer_class = claser
    queryset = student.objects.all()
    pagination_class = PageNumberPagination