from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from selection import services
import requests
from selection.models import Circuits, DriverStandings, Drivers, LapTimes, Races, Results

class HomePageView(View):
  def get (self, request, *args, **kwargs):
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

class SeasonPageView(View):
  def get (self, request, *args, **kwargs):
    selectedRaceId = self.kwargs['raceId']
    selectedYear = self.kwargs['year']
    raceName = None
    raceResults = []
    rawResults = Results.objects.filter(raceId=selectedRaceId).order_by('position')
    for item in rawResults:
      if (raceName == None):
        raceName = item.raceId.name
      if (item.position == -1):
        item.position = 99
      else:
        item.position = item.position
      raceResults.append(item)
    return render(request, 'results.html', context={'results': raceResults, 'year': selectedYear, 'raceName': raceName, 'raceId': selectedRaceId})

class DriverPageView(View):
  def get (self, request, *args, **kwargs):
    _driverData = Drivers.objects.get(driverId=self.kwargs['driverId'])
    _raceData = Races.objects.get(raceId=self.kwargs['raceId'])
    _year = self.kwargs['year']
    _resultsData = Results.objects.all().filter(raceId=self.kwargs['raceId']).filter(driverId=self.kwargs['driverId'])
    _wikiData = services.getWikiData(_driverData.url)
    return render(request, 'driver-detail.html', context={'driverData': _driverData, 'raceData': _raceData, 'year': _year, 'wikiData': _wikiData, 'resultsData': _resultsData })
