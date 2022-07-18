from django.shortcuts import render


def base(request):
    return render(request, template_name="bases/base.html")


def dashboard(request):
    return render(request, template_name="dashboard/dashboard.html")

