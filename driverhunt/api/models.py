from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Driver(User):  # already have first and last name, login, password
    driverid = models.IntegerField(unique=True)  # ID from different service
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'username: {self.username}, driverid: {self.driverid}'


class Position(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='positions')
    x_longitude = models.DecimalField(decimal_places=20, max_digits=100)
    y_latitude = models.DecimalField(decimal_places=20, max_digits=100)
    lastupdate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['lastupdate']

    def __str__(self):
        return f'driver: {self.driver.driverid}: {self.x_longitude}, Y: {self.y_latitude}, update: {self.lastupdate}'
