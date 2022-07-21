import uuid

from django.db import models

from Clients.models import Clients
from Visio.models import Sensor, Team


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    project_name = models.CharField(max_length=1000)
    total_sensors = models.CharField(max_length=20, null=True, blank=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Projects"
        verbose_name_plural = "Projects"


class Building(models.Model):
    building_name = models.CharField(max_length=2000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.building_name

    class Meta:
        verbose_name = "Buildings"
        verbose_name_plural = "Buildings"


class Floor(models.Model):
    floor_name = models.CharField(max_length=1500)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.floor_name

    class Meta:
        verbose_name = "Floors"
        verbose_name_plural = "Floors"


class InstalledSensor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    sensor_label = models.CharField(max_length=500)
    min_range = models.IntegerField(null=True, blank=True)
    max_range = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=1000)

    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    alert_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.sensor_label

    class Meta:
        verbose_name = "Installed Sensors"
        verbose_name_plural = "Installed Sensor"
