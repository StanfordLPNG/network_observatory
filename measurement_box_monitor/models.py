from django.db import models

# Create your models here.
class MeasurementBoxCheckin(models.Model):
    hostname = models.CharField(max_length=256)
    datetime = models.DateTimeField('checkin time')
    choice_text = models.CharField(max_length=400)
