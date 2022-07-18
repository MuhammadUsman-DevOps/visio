import uuid

from django.db import models


class Clients(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    full_name = models.CharField(max_length=1000)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=100)

    contact_person_name = models.CharField(max_length=500, null=True, blank=True)
    contact_person_email_address = models.EmailField(null=True, blank=True)
    contact_person_phone_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"


