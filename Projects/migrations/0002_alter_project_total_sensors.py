# Generated by Django 3.2.13 on 2022-07-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='total_sensors',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
