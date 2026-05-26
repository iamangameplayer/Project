from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict_knn/', views.predict_knn, name='predict_knn'),
]