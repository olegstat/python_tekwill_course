from django.urls import path
from rest_app import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    path('fancy-cats/', views.FancyCatListView.as_view(), name='fancy-cat-list'),
    path('fancy-cats/<int:pk>/', views.FancyCatDetailView.as_view()),
    path('fluffy-tigers/', views.FluffyTigerListView.as_view(), name='fluffy-tiger-list'),
    path('fluffy-tigers/<int:pk>/', views.FluffyTigerDetailView.as_view()),
    path('api-token-auth/', rest_views.obtain_auth_token)
]

