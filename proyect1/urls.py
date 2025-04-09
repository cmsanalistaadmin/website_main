# urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.login_view, name='login'),
    path('supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('vendedor/', views.vendedor_dashboard, name='vendedor_dashboard'),
    path('jefe/', views.jefe_dashboard, name='jefe_dashboard'),
    path('vendedor/formeeff/',views.formeeff, name='formeeff'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    # Agrega otras vistas aquí
]
