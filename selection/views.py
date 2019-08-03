from django.shortcuts import render
from django.http import HttpResponse
from selection import services
import requests
from selection.models import Circuits, DriverStandings, Drivers, LapTimes, Races, Results

def home (request):
  if (request.method == 'GET'):
    selectedYear = request.GET.get('year','2000')
    races = Races.objects.filter(year=selectedYear)
    return render(request, 'select.html', context={'races': races, 'year': selectedYear})

def results (request, year, raceId):
  # if (request.method == 'GET'):
    # selectedYear = request.GET.get('year','')
    print("selectedYear - ", year)
    raceResults = []
    rawResults = Results.objects.filter(raceId=raceId)
    for item in rawResults:
      if (item.position == -1):
        item.position = 99
        print(item.position)
      else:
        item.position = item.position
        print(item.position)
      raceResults.append(item)

    print("Result - ", raceResults)


    return render(request, 'results.html', context={'results': raceResults})
