from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def all_projects(request):
    return render(request, template_name="projects/projects.html")


def project_details(request):
    return render(request, template_name="projects/project_details.html")


def installed_sensors(request):
    return render(request, template_name="projects/installed_sensors.html")


def project_alerts(request):
    return render(request, template_name="projects/alerts.html")


def project_settings(request):
    return render(request, template_name="projects/settings.html")


def sensor_details(request):
    return render(request, template_name="sensors/sensor_details.html")


def files(request):
    return render(request, template_name="projects/files.html")


@require_POST
@csrf_exempt
def test_endpoint(request):
    print(request)

    return redirect("dashboard")

