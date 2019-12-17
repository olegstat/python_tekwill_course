from django.urls import path
from new_app import views

urlpatterns = [
    path('content/', views.content),
    path('ny_days/', views.ny_days),
    path('random/', views.random_numb),
    path('date/', views.date_time),
    path('', views.my_first_view)
]