"""phyto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dashboard.views import SettingsView, plant_page, gallery_page, create_plant, complete_plant, delete_plant

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plant_page, name='plants'),
    path('settings', SettingsView.as_view(), name='settings'),
    path('gallery', gallery_page, name='gallery'),
    path('create-plant]/', create_plant, name='create-plant'),
    path('complete-plant/<int:pk>/', complete_plant, name='complete-plant'),
    path('delete-plant/<int:pk>/', delete_plant, name='delete-plant')
]
