import datetime

from django.shortcuts import render, redirect

from Clients.models import Clients
from Projects.models import Project, Building, InstalledSensor


def add_customer(request):
    if request.method == "POST":
        client_number = Clients.objects.count()
        client_number += 1
        account_id = datetime.date.today().year
        account_id = str(account_id) + str(client_number)

        client = Clients.objects.create(
            account_id=account_id,
            full_name=request.POST.get("full_name"),
            email_address=request.POST.get("email_address"),
            phone_number=request.POST.get("phone_number"),
            address_line=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip_code=request.POST.get("postcode"),
            country=request.POST.get("country"),
            contact_person_name=request.POST.get("contact_person_name"),
            contact_person_email_address=request.POST.get("contact_email_address"),
            contact_person_phone_number=request.POST.get("contact_phone_number"),
        )
        client.save()
        return redirect("customer_details", client.id)

    return render(request, template_name="customers/getting_started.html")


def customer_listing(request):
    customers = Clients.objects.all()
    context = {
        "customers": customers
    }
    return render(request, template_name="customers/customer_listing.html", context=context)


def customer_details(request, client_id):
    client = Clients.objects.get(id=client_id)
    projects = Project.objects.filter(client=client)
    buildings = Building.objects.filter(project__client=client)
    sensors = InstalledSensor.objects.filter(project__client=client)


    context = {
        "client": client,
        "projects": projects,
        "buildings": buildings,
        "sensors": sensors,
    }
    return render(request, template_name="customers/customer_details.html", context=context)


