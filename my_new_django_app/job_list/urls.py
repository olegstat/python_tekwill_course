from django.urls import path
from job_list import views

urlpatterns = [
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/<int:job_id>/', views.job_detail_view, name='job-detail'),
    path('add-job/', views.add_job, name='add-job'),
    path('active-jobs/', views.active_jobs, name='active-jobs')
]