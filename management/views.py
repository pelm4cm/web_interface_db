# Файл: ~/web_interface_db/management/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Clients, Directors
from .forms import ClientWithDirectorForm

@login_required
def index(request):
    clients_count = Clients.objects.count()
    directors_count = Directors.objects.count()
    context = {
        'clients_count': clients_count,
        'directors_count': directors_count,
    }
    return render(request, 'management/index.html', context)

@login_required
def clients_list(request):
    # ИСПРАВЛЕНО: 'client_name' заменено на правильное имя поля 'tszh_name'
    clients = Clients.objects.all().order_by('tszh_name')
    context = {'clients': clients}
    return render(request, 'management/clients_list.html', context)

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientWithDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('db_clients_list')
    else:
        form = ClientWithDirectorForm()
    
    return render(request, 'management/client_create.html', {'form': form})

@login_required
def clients_query_builder(request):
    context = {} # Ваша логика здесь
    return render(request, 'management/clients_query_builder.html', context)
