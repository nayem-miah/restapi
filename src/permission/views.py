from first_app.models import Agent
from first_app.serializers import Agent_serializer
from rest_framework import generics, permissions


class List_api(generics.ListAPIView): # to query a list of data
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    permission_classes = [permissions.IsAuthenticated]







class List_create(generics.ListCreateAPIView): # to query & to create data 
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer


class Retrive(generics.RetrieveAPIView): # to query a single data
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'



class Retrive_update(generics.RetrieveUpdateAPIView): # to query & update a single data
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'


class Retrive_destroy(generics.RetrieveDestroyAPIView): # to query & destroy a single data
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'


class Retrive_update_destroy(generics.RetrieveUpdateDestroyAPIView): # to query, update & destroy a single data
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'






