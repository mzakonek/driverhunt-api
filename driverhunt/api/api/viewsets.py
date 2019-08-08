from api.models import Driver, Position
from .serializers import DriverSerializer, PositionSerializer, LastPositionSerializer
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
import datetime as dt


class DriverViewSet(viewsets.ViewSet):
    # list, create, retrieve, update, partial_update, destroy
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def list(self, request):
        queryset = Driver.objects.all()
        #serializer = DriverSerializer(queryset, many=True)
        serializer = LastPositionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Driver.objects.all()
        driver = get_object_or_404(queryset, driverid=pk)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)

    def create(self, request):
        username_ = request.data['username']
        password = request.data['password']
        driverid = request.data['driverid']

        driver = Driver.objects.create_user(username=username_, password=password, driverid=driverid)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)


class PositionViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def retrieve(self, request, pk=None):
        positions = Position.objects.all()
        drivers = Driver.objects.all()
        driver = get_object_or_404(drivers, driverid=pk)
        position = positions.filter(driver=driver).order_by('lastupdate').last()
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def create(self, request):
        driverid = request.data['driverid']
        x_longitude = request.data['longitude']
        y_latitude = request.data['latitude']

        queryset = Driver.objects.all()
        driver = get_object_or_404(queryset, driverid=int(driverid))

        position = Position.objects.create(driver=driver, x_longitude=x_longitude, y_latitude=y_latitude)
        serializer = PositionSerializer(position)

        return Response(serializer.data)

    #
# class DriverViewSet(viewsets.ModelViewSet):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

# class PositionViewSet(viewsets.ModelViewSet):>>> position = get_object_or_404(

#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
