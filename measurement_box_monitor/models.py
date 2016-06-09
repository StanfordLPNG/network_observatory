from django.db import models

# Create your models here.
class MeasurementBoxCheckin(models.Model):
    hostname = models.CharField(max_length=256, primary_key=True)
    datetime = models.DateTimeField('checkin time', primary_key=True)
    choice_text = models.CharField(max_length=400)
