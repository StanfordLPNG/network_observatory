from django.contrib import admin

# Register your models here.
from .models import MeasurementBoxCheckin, MeasurementBox
admin.site.register(MeasurementBoxCheckin)
admin.site.register(MeasurementBox)
