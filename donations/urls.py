from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('donate/<int:campaign_id>/', views.donate, name='donate'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='donations/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]