from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from selection import services
import requests
from django.contrib import messages
from selection.models import Circuits, DriverStandings, Drivers, LapTimes, Races, Results

def home (request):
  if (request.method == 'GET'):
    selectedYear = request.GET.get('year','1')
    if selectedYear == '1':
      return render(request, 'home.html')
    elif (int(selectedYear) > 1949 and int(selectedYear) < 2019):
      races = Races.objects.filter(year=selectedYear)
      return render(request, 'select.html', context={'races': races, 'year': selectedYear})
    else:
      messages.info(request, 'Please enter a year between 1949 and 2019.')
      selectedYear = None
      return render(request, 'home.html')

def results (request, year, raceId):
  if (request.method == 'GET'):
    selectedYear = request.GET.get('year','')
    raceResults = []
    rawResults = Results.objects.filter(raceId=raceId)
    for item in rawResults:
      if (item.position == -1):
        item.position = 99
      else:
        item.position = item.position
      raceResults.append(item)
    return render(request, 'results.html', context={'results': raceResults})
