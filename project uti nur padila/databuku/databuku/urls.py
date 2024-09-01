from django.contrib import admin
from django.urls import path, include
from .views import DataBukuHomeView


urlpatterns = [
    path('novel/',include(('novel.urls','novel'), namespace='novel')),
    path('', DataBukuHomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    
]


