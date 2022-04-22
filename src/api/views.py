from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Tast
from .serializers import TastSerializer

# Create your views here.
@api_view(['GET'])  #here GET means to get 
def apiOverView(request):

    api_url = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
        
    }

    return Response(api_url) #api_url will 

@api_view(['GET'])
def tastList(request):
    tast = Tast.objects.all()
 
    serializer = TastSerializer(tast, many = True) # data will be serialied
   
    return Response(serializer.data)

@api_view(['GET'])
def tastDetail(request, pk):
    tast = Tast.objects.get(id = pk)
 
    serializer = TastSerializer(tast, many = False)
   
    return Response(serializer.data)

@api_view(['POST']) #here POST means to post
def tastCreate(request):
    
    serializer = TastSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)


@api_view(['POST'])
def tastUpdate(request,pk):

    tast = Tast.objects.get(id = pk)
    serializer = TastSerializer(instance=tast,data = request.data)
    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)



@api_view(['DELETE'])
def tastDelete(request,pk):
 
    tast = Tast.objects.get(id = pk)
    tast.delete()

   
    return Response('Im successfully deleted')