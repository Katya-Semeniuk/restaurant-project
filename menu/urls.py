from . import views
from django.urls import path


urlpatterns = [
    path('food_menu', views.food_menu, name='food_menu'),
    path('drink_menu', views.drink_menu, name='drink_menu'),
]