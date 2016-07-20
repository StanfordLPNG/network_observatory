from django.db import models

# Create your models here.
class MeasurementBoxCheckin(models.Model):
    hostname = models.CharField(max_length=256)
    datetime = models.DateTimeField('checkin time')
    git_head = models.CharField(max_length=40)
    temp = models.DecimalField(max_digits=4, decimal_places=1)
    uptime = models.CharField(max_length=256, default='')

class MeasurementBox(models.Model):
    hostname = models.CharField(max_length=256)
    hardware = models.CharField(max_length=256)
    software = models.CharField(max_length=256)
    connection_type = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    notes = models.CharField(max_length=1024, blank=True)
