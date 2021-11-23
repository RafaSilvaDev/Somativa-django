from django.contrib import admin
from django.urls import path, include
from paciente import views
from home import views as home_views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('mydashboard/', views.dashboard, name='dash'),
    path('', home_views.index, name='index'),
    path('logout/', views.logout, name='logout'),
]
