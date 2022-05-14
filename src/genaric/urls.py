
from django.urls import path
from first_app.serializers import Agent_serializer
from . import views

urlpatterns = [
    path('', views.List_api.as_view()),
    path('list-create/', views.List_create.as_view()),
    path('retrive/<str:pk>/', views.Retrive.as_view(), name="retrive-detail"),
    path('retrive-update/<str:pk>/', views.Retrive_update.as_view(),name="update"),
    path('retrive-destroy/<str:pk>/', views.Retrive_destroy.as_view()),
    path('retrive-update-destroy/<str:pk>/', views.Retrive_update_destroy.as_view()),
    

]
