from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='db_index'),
    path('clients/', views.clients_list, name='db_clients_list'),
    path('clients/add/', views.client_create, name='db_client_create'),
    path('clients/query/', views.clients_query_builder, name='db_clients_query_builder'),
]
