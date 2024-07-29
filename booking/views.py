from django.shortcuts import render
from .models import Reservation

# Create your views here.


def booking(request):

  data = Reservation.objects.all()

  return render(
    request,
    "booking/booking.html",
    {"booking": data}
  )