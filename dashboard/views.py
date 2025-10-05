# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import User

# ------------------------------
# LOGIN CMS
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # Guardamos JWT en sesión para futuras peticiones desde frontend (opcional)
            refresh = RefreshToken.for_user(user)
            request.session['access_token'] = str(refresh.access_token)
            return redirect('dashboard-home')
        else:
            return render(request, 'dashboard/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'dashboard/login.html')


# ------------------------------
# ADMIN CHECK
# ------------------------------
def is_admin(user):
    return user.is_superuser or getattr(user, 'role', '') == 'admin'


# ------------------------------
# DASHBOARD HOME
# ------------------------------
@login_required
def home(request):
    # Solo mostrar botones si es admin
    is_admin_flag = request.user.is_superuser or getattr(request.user, 'role', '') == 'admin'
    return render(request, 'dashboard/home.html', {'is_admin': is_admin_flag})


# ------------------------------
# LISTA DE USUARIOS (Solo Admin)
# ------------------------------
@login_required
@user_passes_test(is_admin)
def user_list_view(request):
    users = User.objects.all()
    return render(request, 'dashboard/user_list.html', {'users': users})


# ------------------------------
# CREAR USUARIO (Solo Admin)
# ------------------------------
@login_required
@user_passes_test(is_admin)
def user_create_view(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if username and password and role:
            User.objects.create_user(username=username, email=email, password=password, role=role)
            message = f'Usuario {username} creado correctamente.'

    return render(request, 'dashboard/user_create.html', {'message': message})
