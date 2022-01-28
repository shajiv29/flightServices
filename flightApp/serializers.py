from .models import Flight, Passenger, Reservation
from rest_framework import serializers

#re regular expression
import re

#Third validation way
def isFlightNumberValid(data):
    print(data)
    print("isFlightNumber")

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'
        #call the validation function
        validators=[isFlightNumberValid]

        #One validation way
    def validate_flightNumber(self, flightNumber):
        if(re.match("^[a-zA-Z0-9]*$", flightNumber)==None):
            raise serializers.ValidationError("Invalid Flight Number. Make Sure It is alpha numberic!!!!")
        return flightNumber


        #second validation way

    def validate(self, data):
        print("validate")
        print(data)
        return data



class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Passenger
        fields='__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
