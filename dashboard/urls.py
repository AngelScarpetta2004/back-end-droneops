from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('login/', views.login_view, name='dashboard-login'),
    path('users/', views.user_list_view, name='dashboard-user-list'),
    path('users/create/', views.user_create_view, name='dashboard-user-create'),
]