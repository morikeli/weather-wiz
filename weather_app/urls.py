from django.urls import path
from weather_app import views

urlpatterns = [
    path('index/', views.index_view, name='index'),

]