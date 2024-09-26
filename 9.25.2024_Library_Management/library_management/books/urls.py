from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.book_list, name="book_list"),
]