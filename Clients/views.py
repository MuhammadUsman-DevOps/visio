from django.shortcuts import render


def add_customer(request):
    return render(request, template_name="customers/getting_started.html")


def customer_listing(request):
    return render(request, template_name="customers/customer_listing.html")


def customer_details(request):
    return render(request, template_name="customers/customer_details.html")


