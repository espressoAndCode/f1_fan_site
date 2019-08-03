from django.shortcuts import render
from django.http import HttpResponse
from selection import services
import requests, csv

from selection.models import Circuits, DriverStandings, Drivers, LapTimes, Races, Results

from datetime import datetime

path='../../f1DB_imgs/f1db_csv/results.csv'

# def home (request):
#   if (request.method == 'GET'):
#     print('Executing GET request')
  #   return render(request, 'select.html')
  # if (request.method == 'POST'):
  #   year = request.POST.get('year','')
  #   # year = '2000'
  #   data = services.get_data(year)
  #   print(f"Data = {data['seasonData']}")
  #   return render(request, 'select.html', {'items': data['seasonData']})

    # with open(path) as f:
    #   reader = csv.reader(f)
    #   for row in reader:
    #     print(row)
        # fields = row.split(',')
        # Circuits.objects.get_or_create(
        #   circuitId   =row[0],
        #   circuitRef  =row[1],
        #   name        =row[2],
        #   location    =row[3],
        #   country     =row[4],
        #   lat         =row[5],
        #   lng         =row[6],
        #   alt         =row[7],
        #   url         =row[8],
        #     )

        # DriverStandings.objects.get_or_create(
        #   driverStandingsId =row[0],
        #   raceId            =row[1],
        #   driverId          =row[2],
        #   points            =row[3],
        #   position          =row[4],
        #   positionText      =row[5],
        #   wins              =row[6],
        # )

        # if (row[2] == '\\N'):
        #   number = -1
        # else:
        #   number = row[2]
        # number = null if (row[2]=='\N') else row[2]
        # Drivers.objects.get_or_create(
        #   driverId    =row[0],
        #   driverRef   =row[1],
        #   number      =number,
        #   code        =row[3],
        #   forename    =row[4],
        #   surname     =row[5],
        #   dob         =row[6],
        #   nationality =row[7],
        #   url         =row[8],

        # )


        # LapTimes.objects.get_or_create(
        #   raceId      =row[0],
        #   driverId    =row[1],
        #   lap         =row[2],
        #   position    =row[3],
        #   time        =row[4],
        #   milliseconds=row[5],
        # )
        # print("oldDate - ", row[5])
        # oldDate = datetime.strptime(row[5], "%m/%d/%y")
        # date = datetime.strftime(oldDate, "%Y-%m-%d")
        # print("Date - ", date)


        # Races.objects.get_or_create(
        #   raceId    =row[0],
        #   year      =row[1],
        #   round     =row[2],
        #   circuitId =row[3],
        #   name      =row[4],
        #   date      =date,
        #   time      =row[6],
        #   url       =row[7],
        # )


        # Results.objects.get_or_create(
        #     resultId        =row[0],
        #     raceId          =row[1],
        #     driverId        =row[2],
        #     constructorId   =row[3],
        #     number          =row[4],
        #     grid            =row[5],
        #     position        =row[6],
        #     positionText    =row[7],
        #     positionOrder   =row[8],
        #     points          =row[9],
        #     laps            =row[10],
        #     time            =row[11],
        #     milliseconds    =row[12],
        #     fastestLap      =row[13],
        #     rank            =row[14],
        #     fastestLapTime  =row[15],
        #     fastestLapSpeed =row[16],
        #     statusId        =row[17],
        # )
