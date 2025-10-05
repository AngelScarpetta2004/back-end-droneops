# droneops/urls.py
from django.contrib import admin
from django.urls import path, include
from dashboard.views import login_view, home, user_list_view, user_create_view
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin Django
    path('admin/', admin.site.urls),

    # Login / Logout CMS
    path('login/', login_view, name='dashboard-login'),
    path('logout/', LogoutView.as_view(next_page='dashboard-login'), name='logout'),

    # Dashboard home (requerir login)
    path('', home, name='dashboard-home'),

    # Administración de usuarios (solo admin)
    path('users/', user_list_view, name='dashboard-user-list'),
    path('users/create/', user_create_view, name='dashboard-user-create'),

    # API REST (para frontend o app móvil)
    path('api/users/', include('users.urls')),  # Asegúrate de tener users/urls.py con rutas API

    # JWT API (login)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
