from rest_framework import serializers
from api.models import Driver, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('x_longitude', 'y_latitude', 'lastupdate')


class DriverSerializer(serializers.ModelSerializer):
    positions = PositionSerializer(many=True)

    class Meta:
        model = Driver
        fields = ('driverid', 'username', 'positions')
