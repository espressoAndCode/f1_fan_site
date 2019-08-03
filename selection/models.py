from django.db import models

# Create your models here.
class F1Stats(models.Model):
    year = models.CharField(max_length=4)


class Circuits(models.Model):
    circuitId   = models.IntegerField(primary_key=True)
    circuitRef  = models.CharField(max_length=255)
    name        = models.CharField(max_length=255)
    location    = models.CharField(max_length=255)
    country     = models.CharField(max_length=255)
    lat         = models.FloatField()
    lng         = models.FloatField()
    alt         = models.IntegerField()
    url         = models.URLField()

class DriverStandings(models.Model):
    driverStandingsId = models.IntegerField(primary_key=True)
    raceId            = models.IntegerField()
    driverId          = models.IntegerField()
    points            = models.FloatField()
    position          = models.IntegerField()
    positionText      = models.CharField(max_length=255)
    wins              = models.IntegerField()

class Drivers(models.Model):
    driverId    = models.IntegerField(primary_key=True)
    driverRef   = models.CharField(max_length=255)
    number      = models.IntegerField()
    code        = models.CharField(max_length=3)
    forename    = models.CharField(max_length=255)
    surname     = models.CharField(max_length=255)
    dob         = models.DateField()
    nationality = models.CharField(max_length=255)
    url         = models.URLField()

class LapTimes(models.Model):
    raceId       = models.IntegerField()
    driverId     = models.IntegerField()
    lap          = models.IntegerField()
    position     = models.IntegerField()
    time         = models.CharField(max_length=255)
    milliseconds = models.IntegerField()

class Races(models.Model):
    raceId    = models.IntegerField(primary_key=True)
    year      = models.IntegerField()
    round     = models.IntegerField()
    circuitId = models.ForeignKey(Circuits, on_delete=models.CASCADE)
    name      = models.CharField(max_length=255)
    date      = models.DateField()
    time      = models.TimeField()
    url       = models.URLField()

class Results(models.Model):
    resultId        = models.IntegerField(primary_key=True)
    raceId          = models.ForeignKey(Races, on_delete=models.CASCADE)
    driverId        = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    constructorId   = models.IntegerField()
    number          = models.IntegerField()
    grid            = models.IntegerField()
    position        = models.IntegerField()
    positionText    = models.CharField(max_length=255)
    positionOrder   = models.IntegerField()
    points          = models.FloatField()
    laps            = models.IntegerField()
    time            = models.CharField(max_length=255)
    milliseconds    = models.IntegerField()
    fastestLap      = models.IntegerField()
    rank            = models.IntegerField()
    fastestLapTime  = models.CharField(max_length=255)
    fastestLapSpeed = models.CharField(max_length=255)
    statusId        = models.IntegerField()
