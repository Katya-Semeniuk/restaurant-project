from django.shortcuts import render
from .models import Food, Drink


# Create your views here.


def food_menu(request):
    """
    a view to display the food menu
    """
    food_list = Food.objects.all()
    return render(
        request, 'menu/food_menu.html', {'food_list': food_list})


def drink_menu(request):
    """
    a view to display the drinks menu
    """
    drink_list = Drink.objects.all()
    return render(
        request, 'menu/drink_menu.html', {'drink_list': drink_list})



