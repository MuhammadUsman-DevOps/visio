from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Visio import settings
from Projects import views
urlpatterns = [
    path('', views.all_projects, name="all_projects"),
    path('project/new', views.add_project, name="add_project"),
    path('<uuid:project_id>/details', views.project_details, name="project_details"),
    path('<uuid:project_id>/sensors', views.installed_sensors, name="installed_sensors"),
    path('<uuid:project_id>/alerts', views.project_alerts, name="project_alerts"),
    path('<uuid:project_id>/settings', views.project_settings, name="project_settings"),
    path('<uuid:project_id>/files', views.files, name="project_files"),

    path('<uuid:project_id>/details', views.sensor_details, name="sensor_details"),
    path('add/building', views.add_building, name="add_building"),

    path('endpoint', views.test_endpoint, name="test_endpoint"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
