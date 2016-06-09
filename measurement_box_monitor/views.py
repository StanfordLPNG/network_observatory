from django.shortcuts import render

from django.http import HttpResponse
from .models import MeasurementBoxCheckin

# Create your views here.
def index(request):

    checkins = MeasurementBoxCheckin.objects.all()

    return render(request, 'checkin.html', {'checkins': checkins })
    #return HttpResponse("Hello world. We made it.")
