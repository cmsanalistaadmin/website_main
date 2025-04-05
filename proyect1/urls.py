# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('vendedor/', views.vendedor_dashboard, name='vendedor_dashboard'),
    path('jefe/', views.jefe_dashboard, name='jefe_dashboard'),
    # Agrega otras vistas aquí
]
