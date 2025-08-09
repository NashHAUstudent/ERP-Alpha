from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'),

    path('', views.erp_dashboard, name='user_erp_dashboard'),
]