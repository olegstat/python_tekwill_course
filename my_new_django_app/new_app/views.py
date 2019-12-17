from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, FileResponse
from datetime import date, datetime
import random
import os, sys
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

# Create your views here.

@csrf_exempt
def my_first_view(request):
    return HttpResponse("Hello world!")

#ex_1
def date_time(request):
    t = datetime.today()
    return HttpResponse('Date and time is: {}'.format(t))

#ex_2
def random_numb(request):
    n = random.random()
    return HttpResponse(n)

#ex_3
def ny_days(request):
    ny = date(2019, 12, 31)
    today = date.today()
    count = ny - today
    return HttpResponse('Until New Year is: {}'.format(count))

#ex_4
def content(request):
    cont_list = []
    path = 'C:/Users/user/Desktop/Curs de Python/python_tekwill_course/my_new_django_app/new_app'
    content = os.listdir(path)
    for var in content:
        cont_list.append(' \n{}'.format(var))
    return HttpResponse(cont_list)

#ex_5
@csrf_exempt
def get_username(request):
    username = request.POST.get('login')
    print(request.POST)
    return HttpResponse(f"Hello, {username}")

#ex_6
def get_sc_pt(request):
    s = request.scheme
    p = request.path
    return HttpResponse(f'Scheme is: {s}. Path is: {p}')

#ex_7, ex_8
@csrf_exempt
def file_saver(request):
    file = request.FILES['file']
    fs = FileSystemStorage()
    fs.save(file.name, file)
    #returning file content as response
    return FileResponse(open('test.txt', 'rb'))

