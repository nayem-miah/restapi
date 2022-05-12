from re import M
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from first_app.models import Agent
from first_app.serializers import Agent_serializer
from rest_framework import permissions
from rest_framework import authentication
from .mixin import MixAuth,MixPermission



#aamrteg





# class Index(APIView):
#     def get(self,request):

#         data = Agent.objects.all()
#         serializers = Agent_serializer(data, many=True)

#         return Response(serializers.data)

# class Index(generics.ListAPIView):
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer

    # permission_classes = [permissions.IsAuthenticated] # default IsAuthenticated in settings.py
    # authentication_classes = [  # default TokenAuthentication in settings.py
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    #     ]



## mixin permission and authentication
## in mixin, we can also use serializer_class and other business logic to reduce code

class Index(generics.ListAPIView, MixPermission, MixAuth):
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    