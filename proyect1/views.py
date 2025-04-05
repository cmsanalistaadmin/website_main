from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Autenticar usando el email como username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            
            # Redirigir según el cargo
            if user.profile.cargo == 'vendedor':
                return redirect('vendedor_dashboard')
            elif user.profile.cargo == 'supervisor':
                return redirect('supervisor_dashboard')
            elif user.profile.cargo == 'jefe':
                return redirect('jefe_dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    
    return render(request, 'duo/login.html')


@login_required
def supervisor_dashboard(request):
    return render(request, 'supervisor/dashboard.html')

@login_required
def vendedor_dashboard(request):
    return render(request, 'vendedor/dashboardven.html')

@login_required
def jefe_dashboard(request):
    return render(request, 'jefe/maindas.html')
