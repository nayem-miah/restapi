from rest_framework import serializers, status, permissions
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView
from first_app.models import Agent
from first_app.serializers import Agent_serializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics


#****************************************************************************
# Create your views here

# # generics
# class List_api(ListAPIView):   #to have a list of data 
#     permission_classes = (permissions.AllowAny,)
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer



# mixins
# class Retrive_api(generics.GenericAPIView,
#             #    mixins.ListModelMixin,
#                mixins.RetrieveModelMixin
               
#                ):

#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):

#         print('check......', args)
#         print('check......', kwargs)


#         return self.list(request,*args, **kwargs)



#APIView 
class List_api(APIView):

    def get(self, request, format=None):
        snippets = Agent.objects.all()
        serializer = Agent_serializer(snippets, many=True)
        return Response(serializer.data)



#****************************************************************************

## generics
# class List_Create(ListCreateAPIView): #to have a list of data and to create
#     permission_classes = (permissions.AllowAny,)
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer


#APIView 
class List_Create(APIView):

    def get(self, request, format=None):
        snippets = Agent.objects.all()
        serializer = Agent_serializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Agent_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





#****************************************************************************

## generics
# class Retrive_api(RetrieveAPIView):   # to have a single data 
#     permission_classes = (permissions.AllowAny,)
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer
#     lookup_field = 'pk'


#APIView 
class Retrive_api(APIView):

    def get(self, request, pk, format=None):
        snippets = Agent.objects.get(pk=pk)
        serializer = Agent_serializer(snippets)
        return Response(serializer.data)




#****************************************************************************

## generics
# class Retrive_destroy_api(RetrieveDestroyAPIView):   # to have and to delete a single data
#     permission_classes = (permissions.AllowAny,)
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer
#     lookup_field = 'pk'



#APIView 
class Retrive_destroy_api(APIView):



    def get(self, request, pk, format=None):
        snippets = Agent.objects.get(pk=pk)
        serializer = Agent_serializer(snippets)
        return Response(serializer.data)
    
    def delete(self, request, pk, format=None):
        snippet = Agent.objects.get(pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    



#****************************************************************************

## generics
# class Retrive_update_api(RetrieveUpdateAPIView):   # to have and to update a single data
#     permission_classes = (permissions.AllowAny,)
#     queryset = Agent.objects.all()
#     serializer_class = Agent_serializer
#     lookup_field = 'pk'



#APIView 
class Retrive_update_api(APIView):

    def get(self, request, pk, format=None):
        snippets = Agent.objects.get(pk=pk)
        serializer = Agent_serializer(snippets)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = Agent.objects.get(pk=pk)
        serializer = Agent_serializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)