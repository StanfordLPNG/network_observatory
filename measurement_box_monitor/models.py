from django.db import models

# Create your models here.
class MeasurementBoxCheckin(models.Model):
    hostname = models.CharField(max_length=256)
    datetime = models.DateTimeField('checkin time')
    git_head = models.CharField(max_length=40)
    temp = models.DecimalField(max_digits=4, decimal_places=1)
