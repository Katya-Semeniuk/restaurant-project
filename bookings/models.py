from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    """
    a class for the Table model
    """
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} ({self.seats} seats)"




class Booking(models.Model):
    """
    a class for the Booking model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    class Meta:
        unique_together = ['table', 'date', 'time']

    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"