from rest_framework import serializers, status, permissions
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from first_app.models import Agent
from first_app.serializers import Agent_serializer

# Create your views here.
class List_api(ListAPIView):   #to have a list of data 
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer



class List_Create(ListCreateAPIView): #to have a list of data and to create
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer


class Retrive_api(RetrieveAPIView):   # to have a single data 
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'


class Retrive_destroy_api(RetrieveDestroyAPIView):   # to have and to delete a single data
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'


class Retrive_update_api(RetrieveUpdateAPIView):   # to have and to update a single data
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'
