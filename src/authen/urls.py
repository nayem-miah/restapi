from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 



urlpatterns = [


    path('',obtain_auth_token), 
    path('list/', views.List_api.as_view()),
    path('list-create/', views.List_create.as_view()),
    path('retrive/<str:pk>/', views.Retrive.as_view()),
    path('retrive-update/<str:pk>/', views.Retrive_update.as_view()),
    path('retrive-destroy/<str:pk>/', views.Retrive_destroy.as_view()),
    path('retrive-update-destroy/<str:pk>/', views.Retrive_update_destroy.as_view()),
    
]


