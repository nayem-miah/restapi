

from django.urls import path
from . import views

urlpatterns = [

    path('', views.List_api.as_view()),
    path('list-create/', views.List_Create.as_view()),
    path('retrive/<str:pk>/', views.Retrive_api.as_view()),
    path('retrive-destroy/<str:pk>/', views.Retrive_destroy_api.as_view()),
    path('retrive-update/<str:pk>/', views.Retrive_update_api.as_view()),

]
