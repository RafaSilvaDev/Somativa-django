from django.urls import path
from paciente import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('mydashboard/', views.dashboard, name='dash'),
    path('buscar/', views.buscar, name='buscar'),
    path('logout/', views.logout, name='logout'),
]
