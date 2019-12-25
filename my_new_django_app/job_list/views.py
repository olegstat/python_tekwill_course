from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPost
from django.http import HttpResponse
from django.urls import reverse
from job_list.forms import JobPostForm
from datetime import datetime

def job_list(request):
    job_list = JobPost.objects.order_by('-date')
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
    active_jobs = JobPost.objects.filter(due_date__gte = datetime.now())
    return render(request, 'active_jobs.html', {'active_jobs': active_jobs})