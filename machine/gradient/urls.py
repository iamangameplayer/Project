from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict_gradient/', views.predict_gradient, name='predict_gradient'),

]