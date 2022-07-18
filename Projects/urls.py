from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Visio import settings
from Projects import views
urlpatterns = [
    path('', views.all_projects, name="all_projects"),
    path('project/details', views.project_details, name="project_details"),
    path('project/sensors', views.installed_sensors, name="installed_sensors"),
    path('project/alerts', views.project_alerts, name="project_alerts"),
    path('project/settings', views.project_settings, name="project_settings"),
    path('project/files', views.files, name="project_files"),
    path('sensor/details', views.sensor_details, name="sensor_details"),

    path('endpoint', views.test_endpoint, name="test_endpoint"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
