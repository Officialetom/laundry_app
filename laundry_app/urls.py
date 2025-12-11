from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/add/', views.add_order, name='add_order'),
    path('order/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('order/delete/<int:pk>/', views.delete_order, name='delete_order'),
    path('payment/add/', views.add_payment, name='add_payment'),
]
