from django.urls import path
from atc import views

urlpatterns = [path('', views.hello_world, name='hello_world'), ]