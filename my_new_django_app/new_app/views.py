from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
import random
import os, sys
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def my_first_view(request):
    print("hello")
    return HttpResponse("Hello world!")

def date_time(request):
    t = datetime.today()
    return HttpResponse('Date and time is: {}'.format(t))

def random_numb(request):
    n = random.random()
    return HttpResponse(n)

def ny_days(request):
    ny = date(2019, 12, 31)
    today = date.today()
    count = ny - today
    return HttpResponse('Until New Year is: {}'.format(count))

def content(request):
    cont_list = []
    path = 'C:/Users/user/Desktop/Curs de Python/python_tekwill_course/my_new_django_app/new_app'
    content = os.listdir(path)
    for var in content:
        cont_list.append(' \n{}'.format(var))
    return HttpResponse(cont_list)
