from django.urls import path
from . import views

urlpatterns = [
    path('', views.metrics, name='metrics'),
    path('model_comparison/', views.model_comparison, name='model_comparison'),
]