from django.urls import path
from new_app import views

urlpatterns = [
    path('file_saver/', views.file_saver),
    path('get_sc_pt/', views.get_sc_pt),
    path('get_username/', views.get_username),
    path('content/', views.content),
    path('ny_days/', views.ny_days),
    path('random/', views.random_numb),
    path('date/', views.date_time),
    path('', views.my_first_view)
]