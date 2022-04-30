
from first_app.serializers import Agent_serializer
from first_app.models import Agent
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class List_api(APIView):

    def get(self, request, formant=None):
        queryset = Agent.objects.all()
        serializers = Agent_serializer(queryset, many=True)
        return Response(serializers.data)




class List_create(APIView):

    def get(self, request, formant=None):
        queryset = Agent.objects.all()
        serializers = Agent_serializer(queryset, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = Agent_serializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        


class Retrive(APIView):

    def get(self, request, pk, formant=None):
        queryset = Agent.objects.get(pk=pk)
        serializers = Agent_serializer(queryset)
        return Response(serializers.data)


        

class Retrive_update(APIView):

    def get(self, request, pk,formant=None):
        queryset = Agent.objects.get(pk=pk)
        serializers = Agent_serializer(queryset)
        return Response(serializers.data)

    def put(self, request,pk,format=None):
        queryset = Agent.objects.get(pk=pk)
        serializers = Agent_serializer(queryset,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

        
class Retrive_destroy(APIView):

    
    def pk_id(self, pk):
        try:
            return Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            raise Http404

    def get(self, request, pk,formant=None):
      
        queryset = self.pk_id(pk)
        serializers = Agent_serializer(queryset)
        return Response(serializers.data)

    def delete(self,request, pk, format=None):
        queryset = self.pk_id(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



        

class Retrive_update_destroy(APIView):

    def pk_id(self, pk):
        try:
            return Agent.objects.get(pk=pk)
        except Agent.DoesNotExist:
            raise Http404


    def get(self, request, pk, formant=None):
        queryset = self.pk_id(pk)
        serializers = Agent_serializer(queryset)
        return Response(serializers.data)
        
    def put (self, request, pk, format=None):
        queryset = self.pk_id(pk)
        serializers = Agent_serializer(queryset, data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk,format=None):
        queryset = self.pk_id(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



