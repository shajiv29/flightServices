from django.shortcuts import render
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#filter
from django_filters.rest_framework import DjangoFilterBackend
#search filter
from rest_framework import filters

# auth
from rest_framework.permissions import IsAuthenticated


# Create your views here.
"""
Postman request
{
	"departureCity": "Dhaka",
	"arrivalCity": "Chittagonj",
	"dateOfDeparture": "2022-01-27"
}
"""
@api_view(['POST'])
def find_flights(request):
    flight = Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flight,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def  save_reservation(request):
    flight = Flight.objects.get(id=request.data['flightId'])

    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = ReserVation()
    reservation.flight = flight
    reservation.passenger = passenger

    Reservation.save(reservation)
    return Response(status=status.HTTP_201_CREATED)



class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['flightNumber', 'departureCity', 'arrivalCity']
    # then migrate then auto create database table
    permission_classes = (IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
