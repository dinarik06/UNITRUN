from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.profile, name='profile'),
    path("register/", views.register, name="register"),
    path('tapalka/', views.tapalka, name="tapalka"),
    path('update_balance/', views.update_balance, name="update_balance"),
    path('liveapril_case/', views.liveapril_case, name="liveapril_case"),
    path('liveapril_case/', views.cat_case, name="cat_case"),
    path('liveapril_case/', views.unit_case, name="unit_case"),
    path('liveapril_case/', views.legendary_case, name="legendary_case"),
    path('liveapril_case/', views.ps2_case, name="ps2_case"),
    path("spend-balance/", views.spend_balance, name="spend_balance")
]