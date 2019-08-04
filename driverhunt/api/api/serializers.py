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


class LastPositionSerializer(serializers.ModelSerializer):
    last_position = serializers.SerializerMethodField()

    def get_last_position(self, driver):
        # qs = Position.objects.filter(driver=driver).order_by('-lastupdate')
        try:
            qs = driver.positions.latest('lastupdate')
            serializer = PositionSerializer(qs)
        except:
            return None
        return serializer.data

    class Meta:
        model = Driver
        fields = ('driverid', 'username', 'last_position')

