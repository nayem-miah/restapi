from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('frontend/', TemplateView.as_view(template_name='index.html'),),
    path('api/', include('api.urls')),
    
    path('', include('frontend.urls')),
    path('first/', include('first_app.urls')),
    path('check/', include('test_api.urls')),
    path('genaric/', include('genaric.urls')),
    path('api-view/', include('apiview.urls')),
    path('permission/', include('permission.urls')),
    path('auth/', include('authen.urls')),
    path('auth/view-rouder/', include('authen.rouders')),
]
