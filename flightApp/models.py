from django.db import models

# Create your models here.


class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20, blank=True, null=True)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture= models.TimeField()


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
