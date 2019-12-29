from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPost
from django.http import HttpResponse
from django.urls import reverse
from job_list.forms import JobPostForm, SignUpForm
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth import login as auth_login

def job_list(request):
    jobs= JobPost.objects.order_by('-date')
    paginator = Paginator(jobs, 4)
    page = request.GET.get('page')
    job_list = paginator.get_page(page)
    return render(request, 'job_list.html', {'job_list': job_list})

def job_detail_view(request, job_id):
    job_post = get_object_or_404(JobPost, pk=job_id)
    return render(request, 'job_detail.html', {'job_post': job_post})

def add_job(request):
    if request.method == "GET":
        form = JobPostForm()
        return render(request, 'add_job.html', {'form': form})
    form = JobPostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse(job_list))
    return render(request, 'add_job.html', {'form': form})

def active_jobs(request):
    active_job_list = JobPost.objects.filter(due_date__gte = datetime.now())
    paginator = Paginator(active_job_list, 4)
    page = request.GET.get('page')
    active_jobs = paginator.get_page(page)
    return render(request, 'active_jobs.html', {'active_jobs': active_jobs})

def edit_job(request, job_id):
    job_post = get_object_or_404(JobPost, pk=job_id)
    edit_form = JobPostForm(instance=job_post)
    if request.method == 'POST':
        edit_form = JobPostForm(request.POST, instance=job_post)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse(job_detail_view, args=(job_id, )))
        else:
            edit_form = JobPostForm(instance=job_post)
    return render(request, 'edit_job.html', {'form': edit_form, 'job_post': job_post})

def delete_job(request, job_id):
    job_post = get_object_or_404(JobPost, pk=job_id)
    if request.method == "POST":
        job_post.delete()
        return redirect(reverse(job_list))
    return render(request, 'delete_job.html', {'job_post': job_post})

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('job-list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})