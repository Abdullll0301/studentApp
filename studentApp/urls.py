from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/custom/', views.custom_admin_login, name='custom_admin_login'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('school_items/', views.school_items, name='school_items'),
]
