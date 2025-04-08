from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Autentica usando el email (definido como USERNAME_FIELD)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            # Redirige según el cargo
            if user.cargo == 'vendedor':
                return redirect('vendedor_dashboard')
            elif user.cargo == 'supervisor':
                return redirect('supervisor_dashboard')
            elif user.cargo == 'jefe':
                return redirect('jefe_dashboard')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
            # La redirección se mantiene en el login para poder mostrar el error

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

def logout_view(request):
    logout(request)
    return redirect('login')

def formeeff (request):
    return render(request, 'vendedor/formEEFF.html')
