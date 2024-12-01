"""
URL configuration for unitrun project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from profiles import views

urlpatterns = [
    path("", views.home, name='home'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("tapalka/", views.tapalka, name="tapalka"),
    path('update_balance/', views.update_balance, name="update_balance"),
    path('liveapril_case/', views.liveapril_case, name="liveapril_case"),
    path('cat_case/', views.cat_case, name="cat_case"),
    path('unit_case/', views.unit_case, name="unit_case"),
    path('legendary_case/', views.legendary_case, name="legendary_case"),
    path('ps2_case/', views.ps2_case, name="ps2_case"),
    path('spend-balance/', views.spend_balance, name="spend_balance")
]


