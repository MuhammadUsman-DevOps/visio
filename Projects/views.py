from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from Clients.models import Clients
from Projects.models import Project, Building, InstalledSensor, Floor
from Visio.models import Sensor


@require_POST
def add_project(request):
    client = Clients.objects.get(id=request.POST.get("client"))
    project = Project.objects.create(
        project_name=request.POST.get("project_name"),
        total_sensors=request.POST.get("sensors"),
        client=client,
    )
    project.save()

    return redirect("customer_details",client.id)

def all_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, template_name="projects/projects.html", context=context)


def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="projects/project_details.html", context=context)


def installed_sensors(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="projects/installed_sensors.html", context=context)


def project_alerts(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="projects/alerts.html", context=context)


def project_settings(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="projects/settings.html", context=context)


def sensor_details(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="sensors/sensor_details.html", context=context)


def files(request, project_id):
    project = Project.objects.get(id=project_id)
    project_buildings = Building.objects.filter(project=project)
    project_sensors = InstalledSensor.objects.filter(project=project)
    project_locations = Floor.objects.filter(building__project=project)
    available_sensors = Sensor.objects.all()
    context = {
        "project": project,
        "project_buildings": project_buildings,
        "project_sensors": project_sensors,
        "project_locations": project_locations,
        "available_sensors": available_sensors,
    }
    return render(request, template_name="projects/files.html", context=context)


@require_POST
def add_building(request):
    building = Building.objects.create(
        building_name=request.POST.get("building_name"),
        project=Project.objects.get(id=request.POST.get("project_id"))
    )
    building.save()
    return redirect("project_details",request.POST.get("project_id") )


@require_POST
def add_sensor(request):
    sensor = InstalledSensor.objects.create(

    )

@require_POST
@csrf_exempt
def test_endpoint(request):
    print(request)

    return HttpResponse(status=200)

