from rest_framework.routers import DefaultRouter
from authen.viewset import AgentViewset

rouder = DefaultRouter()

rouder.register('agent-abc', AgentViewset, basename= 'agents')

print(rouder.urls)
urlpatterns = rouder.urls