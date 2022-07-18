from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from Visio import settings
from Clients import views

urlpatterns = [

    path('add-new/', views.add_customer, name="add_customer"),
    path('details', views.customer_details, name="customer_details"),
    path('all/', views.customer_listing, name="customer_listing"),

    path('projects/', include("Projects.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
