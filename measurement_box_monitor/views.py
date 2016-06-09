from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from .models import MeasurementBoxCheckin

# Create your views here.
def index(request):
    checkins = MeasurementBoxCheckin.objects.all()

    return render(request, 'view_checkins.html', {'checkins': checkins })
    #return HttpResponse("Hello world. We made it.")

@csrf_exempt
def do_checkin(request):
    if request.method == "POST":
        try:
            checkin = MeasurementBoxCheckin()
            checkin.hostname = request.POST['hostname']
            checkin.datetime = request.POST['datetime']
            checkin.choice_text = request.POST['payload']
        except Exception as e:
            return HttpResponse("failed to post checkin, error: " + e.message)

        checkin.save()

        return render(request, 'add_checkin.html', {'checkin': checkin })
    else:
        return HttpResponse("checkins done by POST requests only")
