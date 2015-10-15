from django.shortcuts import render
from .models import Make, LubMake, Series, Engine, Car, Lub

# Create your views here.


def index(request):
    return render(request, 'lub/index.html', {})


def car_list(request):
    cars = Car.objects.all()

    context_dict = {
        'cars': cars,
    }

    return render(request, 'lub/car_list.html', context_dict)


def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    manual_listed_lubs = car.manual_listed_lubs.all()

    try:
        engine = Engine.objects.get(series=car.series)
    except Engine.DoesNotExist:
        engine = None

    try:
        matched_lub = Lub.objects.filter(motor_type__contains=car.motor_type,
                                         lub_type__contains=car.lub_type)
    except Lub.DoesNotExist:
        matched_lub = None

    context_dict = {
        'car': car,
        'mll': manual_listed_lubs,
        'engine': engine,
        'matched_lub': matched_lub,
    }

    return render(request, 'lub/car_detail.html', context_dict)


def lub_list(request):
    lubs = Lub.objects.all()

    context_dict = {
        'lubs': lubs,
    }

    return render(request, 'lub/lub_list.html', context_dict)


def lub_detail(request, lub_id):
    lub = Lub.objects.get(pk=lub_id)

    try:
        lub_listed_in_car_manual = Car.objects.filter(manual_listed_lubs__name=lub.name)
    except Lub.DoesNotExist:
        lub_listed_in_car_manual = None

    context_dict = {
        'lub': lub,
        'cars': lub_listed_in_car_manual,
    }

    return render(request, 'lub/lub_detail.html', context_dict)


def lub_match(request):
    return render(request, 'lub/lub_match.html', {})