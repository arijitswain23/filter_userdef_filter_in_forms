from django.shortcuts import render

import datetime
# Create your views here.
def filters(request):
    dt=datetime.datetime.now()
    d={'Data':"So beaUtiFul so eligent Just Looking like wOw",'dt':dt,'c':10}
    return render(request,'filters.html',d)