import pdb
import csv
import requests
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse, JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# Create your views here.

API_KEY = 1

def hello_world(request):
    res = requests.get(f"https://www.thecocktaildb.com/api/json/v1/{ API_KEY }/search.php?s=margarita")
    with open('api/data/global_land.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(row)
    return JsonResponse(res.json())

