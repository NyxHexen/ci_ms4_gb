from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('_payment_intent/', views.create_payment, name='create_payment'),
    path('success/<order_number>', views.checkout_success, name='checkout_success'),
]