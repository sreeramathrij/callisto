from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("year2/s4", views.index)
]