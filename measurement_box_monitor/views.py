from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import datetime

from django.http import HttpResponse
from django.utils import timezone
from .models import MeasurementBoxCheckin

# Create your views here.
def index(request):
    checkins = MeasurementBoxCheckin.objects.order_by('hostname', '-datetime').distinct('hostname')
    one_hour_ago = timezone.now() - datetime.timedelta(hours = 1)
    for checkin in checkins:
        checkin.late = checkin.datetime <= one_hour_ago

    return render(request, 'view_checkins.html', {'checkins': checkins })

@csrf_exempt
def do_checkin(request):
    if request.method == "POST":
        try:
            checkin = MeasurementBoxCheckin()
            checkin.hostname = request.POST['hostname']
            checkin.datetime = request.POST['datetime']
            checkin.git_head = request.POST['head']
            checkin.temp = request.POST['temp']

        except Exception as e:
            return HttpResponse("failed to post checkin, error: " + e.message)

        checkin.save()

        return render(request, 'add_checkin.html', {'checkin': checkin })
    else:
        return HttpResponse("checkins done by POST requests only")
