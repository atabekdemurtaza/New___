from django.urls import path
from .views import ItemView, ItemsView
from django.contrib import admin

urlpatterns = [
    path ('items/', ItemsView),
    path('item/<int:nm>/', ItemView),
]