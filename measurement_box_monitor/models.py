from django.db import models

# Create your models here.
class MeasurementBoxCheckin(models.Model):
    datetime = models.DateTimeField('checkin time')
    choice_text = models.CharField(max_length=200)
