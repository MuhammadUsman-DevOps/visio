from django.shortcuts import render


def base(request):
    return render(request, template_name="bases/base.html")


def dashboard(request):
    return render(request, template_name="dashboard/dashboard.html")


def add_customer(request):
    return render(request, template_name="customers/getting_started.html")


def customer_listing(request):
    return render(request, template_name="customers/customer_listing.html")


def customer_details(request):
    return render(request, template_name="customers/customer_details.html")


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
