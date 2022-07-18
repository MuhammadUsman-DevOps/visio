"""Visio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from Visio import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.base),
    path('', views.dashboard, name="dashboard"),
    path('customers/', include("Clients.urls")),

    path('projects/', views.all_projects, name="all_projects"),
    path('project/details', views.project_details, name="project_details"),
    path('project/sensors', views.installed_sensors, name="installed_sensors"),
    path('project/alerts', views.project_alerts, name="project_alerts"),
    path('project/settings', views.project_settings, name="project_settings"),
    path('project/files', views.files, name="project_files"),
    path('sensor/details', views.sensor_details, name="sensor_details"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
