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






class Reservation(models.Model):
    """
    a class for the Reservation model
    """

    TIME_SLOTS = [
        ('12:00', '12:00 PM'),
        ('13:00', '01:00 PM'),
        ('14:00', '02:00 PM'),
        ('15:00', '03:00 PM'),
        ('16:00', '04:00 PM'),
        ('17:00', '05:00 PM'),
        ('18:00', '06:00 PM'),
        ('19:00', '07:00 PM'),
        ('20:00', '08:00 PM'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=5, choices=TIME_SLOTS)
    guests = models.PositiveIntegerField()

    class Meta:
        unique_together = ['table', 'date', 'time']

    def __str__(self):
        return f"Booking for {self.user} on {self.date} at {self.time}"