# management/urls.py (новый файл)

from django.urls import path
from . import views # импортируем views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/add/', views.client_create, name='client_create'),
    # auth
    path('login/', auth_views.LoginView.as_view(template_name='management/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    # query builder
    path('clients/query/', views.clients_query_builder, name='clients_query_builder'),
]