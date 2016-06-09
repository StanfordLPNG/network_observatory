from django.shortcuts import render

from django.http import HttpResponse
from .models import MeasurementBoxCheckin

# Create your views here.
def index(request):
    checkins = MeasurementBoxCheckin.objects.all()

    return render(request, 'view_checkins.html', {'checkins': checkins })
    #return HttpResponse("Hello world. We made it.")

def do_checkin(request):
    checkin = MeasurementBoxCheckin()
    checkin.save()
    return render(request, 'add_checkin.html', {'checkin': checkin })
