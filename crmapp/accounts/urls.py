from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('create_order/',views.createOrder,name="create_order"),
]
