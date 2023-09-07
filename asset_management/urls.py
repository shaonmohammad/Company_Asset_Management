

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_asset/', views.add_asset, name='add_asset'),
    path('checkout_device', views.check_out_device, name='checkout_device'),

]
