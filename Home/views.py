from django.shortcuts import render
from .models import CarsModel,SingleCarmodel

def homepage(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"home/home.html",context)


def carshow(request):
    car = CarsModel.objects.all()
    
    context={
        "cars":car
    }

    return render(request,"Products/cars.html",context)


def singlecar(request , car_id):
    scar = SingleCarmodel.objects.get(pk = car_id) , SingleCarmodel.objects.all()
    context={
        "scars":scar,
    }

    return render(request,"Products/singlecar.html",context)