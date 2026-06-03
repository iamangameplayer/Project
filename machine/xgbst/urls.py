from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict_xgbst/', views.predict_xgbst, name='predict_xgbst'),
]