from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserProfileData),
    path('order/', views.OrderData),
    path('orderd/', views.OrderDetailsData),
    path('pay/', views.PaymentData),
    path('pro/', views.ProductData),

]
