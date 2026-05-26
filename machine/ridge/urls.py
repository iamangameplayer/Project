from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('predict_ridge/', views.predict_ridge, name='predict_ridge'),
]