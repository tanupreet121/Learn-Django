from django.urls import path
from . import views

urlpatterns = [

    path("<int:month>", views.monthlychallenge_num),
    path("<str:month>", views.monthlychallenge)
]