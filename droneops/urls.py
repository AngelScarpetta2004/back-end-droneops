# droneops/urls.py
from django.contrib import admin
from django.urls import path, include
from dashboard.views import login_view, home, user_list_view, user_create_view
from django.contrib.auth.views import LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('api/users/', include('users.urls')),
    path('login/', login_view, name='dashboard-login'),
    path('logout/', LogoutView.as_view(next_page='dashboard-login'), name='logout'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # APIs de apps
    path('api/drones/', include('drones.urls')),
    path('api/repairs/', include('repairs.urls')),
    path('api/audit/', include('audit.urls')),
    path('api/inventory/', include('inventory.urls')),
    path('api/events/', include('events.urls')),
]
