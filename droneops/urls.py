# droneops/urls.py
from django.contrib import admin
from django.urls import path, include
from dashboard.views import login_view
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # CMS (interfaz web)
    path('', include('dashboard.urls')),

    # API REST (para frontend o app móvil)
    path('api/users/', include('users.urls')),  # ahora la API empieza en /api/users/

    # Autenticación CMS
    path('login/', login_view, name='dashboard-login'),
    path('logout/', LogoutView.as_view(next_page='dashboard-login'), name='logout'),

    # Autenticación API (JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
