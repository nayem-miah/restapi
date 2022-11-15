from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token # create token part 1
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView # simple token 
# from rest_framework.authentication import TokenAuthentication

urlpatterns = [

    path('', views.index, name='index'),
    path('register/', views.registationApi),
    path('login-api/',obtain_auth_token), # create token part 2
    
    path('token',TokenObtainPairView.as_view()), # simple token 
    path('token/refresh',TokenRefreshView.as_view()), # simple token

    path('contact/', views.ContactApiView.as_view(), name='contact'),
    path('list/', views.AgentListView.as_view(), name='list'),
    path('top-seller', views.AgentTopSellerView.as_view(), name='top'),
    path('<pk>', views.AgentDetailView.as_view(), name='detail'),

    path('home/', views.HomeListApiView.as_view(), name='home'),
    path('detail/<slug>/', views.HomeDetailApiView.as_view(), name='detail'),
    path('image/<pk>/', views.ImageView.as_view(), name='image'),


    path('location/', views.LocationAPI.as_view()),


#   # search api not working 
    path('search', views.Search.as_view(), name='search'),





]