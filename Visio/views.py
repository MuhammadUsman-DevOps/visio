from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Clients.models import Clients
from Projects.models import Project
from Visio.models import Team, Sensor


def base(request):
    return render(request, template_name="bases/base.html")


def dashboard(request):
    projects = Project.objects.all().count()
    clients = Clients.objects.all().count()
    team = Team.objects.all().count()
    users = User.objects.all().count()
    sensors = Sensor.objects.all().count()
    context = {
        "projects": projects,
        "clients": clients,
        "team": team,
        "users": users,
        "sensors": sensors,
    }
    return render(request, template_name="dashboard/dashboard.html", context=context)


def auth_login(request):
    if request.method == 'POST':
        username = request.POST.get("email_address")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid login credentials!")

    return render(request, template_name="authentication/signin.html")


def auth_logout(request):
    logout(request)
    return redirect("auth_login")