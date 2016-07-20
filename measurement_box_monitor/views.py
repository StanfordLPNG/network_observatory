from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import datetime

from django.http import HttpResponse
from django.utils import timezone
from .models import MeasurementBoxCheckin, MeasurementBox

# Create your views here.
def index(request):
    checkins = MeasurementBoxCheckin.objects.order_by('hostname', '-datetime').distinct('hostname')
    one_hour_ago = timezone.now() - datetime.timedelta(hours = 1)
    for displayed_checkin in checkins:
        displayed_checkin.late = displayed_checkin.datetime <= one_hour_ago

        # defaults in case hostname is not in MeasurementBox table
        displayed_checkin.hardware = "unknown"
        displayed_checkin.software = "unknown"
        displayed_checkin.connection_type = "unknown" 
        displayed_checkin.location = "unknown" 

        # Only want a single object but use filter and for loop because we don't want website to blow up if one doesn't exist
        box_infos = MeasurementBox.objects.filter(hostname=displayed_checkin.hostname)

        for box_info in box_infos:
            displayed_checkin.hardware = box_info.hardware 
            displayed_checkin.software = box_info.software
            displayed_checkin.connection_type = box_info.connection_type 
            displayed_checkin.location = box_info.location 


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
            if 'uptime' in request.POST:
                checkin.uptime = request.POST['uptime']

        except Exception as e:
            return HttpResponse("failed to post checkin, error: " + e.message)

        checkin.save()

        return render(request, 'add_checkin.html', {'checkin': checkin })
    else:
        return HttpResponse("checkins done by POST requests only")
