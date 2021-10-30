from django.http.response import HttpResponse
from .models import LogSystem
from django.shortcuts import render

def geoLocator(request) :
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if request.method == "GET" :
        lat = request.GET.get("lat")
        long = request.GET.get("long")
    else :
        lat, long = 0,0
    user_agent = request.META['HTTP_USER_AGENT']
    log = LogSystem()
    log.ip = ip
    log.lat = lat
    log.long = long
    log.user_agent = user_agent
    log.save()
    return HttpResponse("Thanks")

def homepage(request) :
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META['HTTP_USER_AGENT']
    log = LogSystem()
    log.ip = ip
    log.user_agent = user_agent
    log.save()
    return render(request, 'index.html')