from django.shortcuts import render

# Create your views here.

def timetable(request):
    return render(request,'webtimetable/timetable.html')

def secmap(request):
    return render(request,'webtimetable/secmap.html')

def firstyearblock(request):
    return render(request,'webtimetable/firstyearblock.html')