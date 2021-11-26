from django.urls import path
from paciente import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastrar, name='cadastro'),
    path('mydashboard/', views.dashboard, name='dash'),
    path('buscarM/', views.buscar_medico, name='buscarM'),
    path('buscarC/', views.buscar_consulta, name='buscarC'),
    path('logout/', views.logout, name='logout'),
]
