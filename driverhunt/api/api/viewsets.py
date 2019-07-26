from api.models import Driver, Position
from .serializers import DriverSerializer, PositionSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, get_list_or_404


class DriverViewSet(viewsets.ViewSet):
    # list, create, retrieve, update, partial_update, destroy
    def list(self, request):
        print(request)
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset, many=True)
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
    def retrieve(self, request, pk=None):
        positions = Position.objects.all()
        drivers = Driver.objects.all()
        driver = get_object_or_404(drivers, driverid=pk)
        position = positions.filter(driver=driver).order_by('lastupdate').last()
        serializer = PositionSerializer(position)
        return Response(serializer.data)

    def create(self, request):
        print(request.data['driverid'], request.data['x_latitude'])

    #
# class DriverViewSet(viewsets.ModelViewSet):
#     queryset = Driver.objects.all()
#     serializer_class = DriverSerializer

# class PositionViewSet(viewsets.ModelViewSet):>>> position = get_object_or_404(

#     queryset = Position.objects.all()
#     serializer_class = PositionSerializer
