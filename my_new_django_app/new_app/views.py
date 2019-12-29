from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest, FileResponse, JsonResponse, StreamingHttpResponse
from datetime import date, datetime
import random
from time import sleep
from time import ctime
import os, sys
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .models import BlogPost
from django.urls import reverse
from .forms import BlogPostForm
from job_list import views

# Create your views here.

@csrf_exempt
def my_first_view(request):
    return redirect(reverse(views.home))

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

def special_case_2003(request):
    print('2003')
    return HttpResponse("Year is 2003")

def year_archive(request, year):
    print(year)
    return HttpResponse(f"Year is {year}")

def month_archive(request, year, month):
    print(year, month)
    return HttpResponse(f'Year is {year}, Month is {month}')

def article_detail(request, year, month, slug):
    print(year, month, slug)
    return HttpResponse(f'Year is {year}, Month is {month}, Slug is {slug}')

def cat_image_view(request):
    return FileResponse(open('cat.jpg', 'rb'))

def json_view(request):
    return JsonResponse({'data': 'value'})

def streaming_writer(rows):
    for row in range(rows):
        yield (f'{row} ')
        sleep(0.5)

def streaming_view(request):
    return StreamingHttpResponse(streaming_writer(100))

#lesson_13_ex_1
def name_age(request):
    return JsonResponse({'name': 'Alice', 'age': "22"})

#lesson_13_ex_2
def time_count(n):
    while n !=0:
        time = ctime()
        yield (f'Current time is: {time} <br>')
        n -=1
        sleep(1)
def current_time(request):
    return StreamingHttpResponse(time_count(10))


def recent_blog_post(request):
    top_5_blog_posts = BlogPost.objects.all().order_by('-date')[:5]
    return render(request, "blog_posts.html", {"recent_blog_post": top_5_blog_posts})

def blog_post_view(request, blog_post_id):
    blog_post = BlogPost.objects.get(id=blog_post_id)
    return render(request, 'blog_post_page.html', {'blog_post': blog_post})

def add_blog_post(request):
    if request.method == 'GET':
        form = BlogPostForm()
        return render(request, 'add_blog_post.html',{'form': form})
    form = BlogPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse(recent_blog_post))
    return render(request, 'add_blog_post.html', {'form': form})

def edit_blog_post(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    edit_form = BlogPostForm(instance=blog_post)
    if request.method == 'POST':
        edit_form = BlogPostForm(request.POST, instance=blog_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse(blog_post_view, args=(blog_post_id, )))
        else:
            edit_form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': edit_form, 'blog_post': blog_post})



