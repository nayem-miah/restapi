
from rest_framework import viewsets
from first_app.models import Agent
from first_app.serializers import Agent_serializer


class AgentViewset(viewsets.ModelViewSet):

    '''
    get--> list 
    get --> retrive a single data
    post --> new instance
    put --> update
    delete --> destroy
    patch --> partial update

    '''
    queryset = Agent.objects.all()
    serializer_class = Agent_serializer
    lookup_field = 'pk'