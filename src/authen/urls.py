from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token 



urlpatterns = [


    path('',obtain_auth_token), 
    path('list/',views.Index.as_view()),


]