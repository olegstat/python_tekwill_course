from django.urls import path
from job_list import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/<int:job_id>/', views.job_detail_view, name='job-detail'),
    path('add-job/', views.add_job, name='add-job'),
    path('active-jobs/', views.active_jobs, name='active-jobs'),
    path('edit-job/<int:job_id>/', views.edit_job, name='edit-job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete-job')
]