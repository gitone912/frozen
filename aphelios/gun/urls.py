
from django.contrib import admin
from django.urls import path,include
from gun import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.loginuser,name='login'),
    path('logout',views.logoutuser,name='logout'),
]
