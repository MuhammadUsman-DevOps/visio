from django.db import models


class Sensor(models.Model):
    sensor_name = models.CharField(max_length=500)
    sensor_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.sensor_name

    class Meta:
        verbose_name = "Available Sensors"
        verbose_name_plural = "Available Sensors"


class Team(models.Model):
    team_name = models.CharField(max_length=500)
    email_addresses = models.TextField()
    phone_numbers = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"

