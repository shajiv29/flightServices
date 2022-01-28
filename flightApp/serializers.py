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


# class ProductSerializer(serializers.ModelSerializer):
# # validation
#
# name = serializers.CharField(error_messages={'blank': 'Please fillout the product name!'})
#
# price = serializers.FloatField(error_messages={'blank': 'Please fillout the product price!'})
#
# slug = serializers.SlugField(error_messages={'blank': 'Please fillout the product slug!'})
#
# size = serializers.CharField(error_messages={'blank': 'Please fillout the product size!'})
#
# description = serializers.CharField(error_messages={'blank': 'Please fillout the description!'})
#
# image = serializers.ImageField(required=False, error_messages={'blank': 'Please upload a photo image!'})
#
# # validation
# category = serializers.StringRelatedField(read_only=False)
# productType = serializers.StringRelatedField()
# user = serializers.StringRelatedField()
#
# def validate(self, data):
#     if "image" not in data:
#         raise serializers.ValidationError("Please upload a photo image!")
#     return data
#
# 
# class Meta:
#     model = Product
#     fields = "__all__"
