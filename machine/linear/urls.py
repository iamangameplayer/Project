from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('predict_linear/', views.predict_linear, name= 'predict_linear'),
]