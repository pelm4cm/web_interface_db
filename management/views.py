from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from .models import Clients
from .forms import ClientWithDirectorForm


staff_required = user_passes_test(lambda u: u.is_authenticated and u.is_staff)


@staff_required
def index(request):
    return render(request, 'management/index.html')


@staff_required
def clients_list(request):
    query_name = (request.GET.get('name') or '').strip()
    query_inn = (request.GET.get('inn') or '').strip()
    query_city = (request.GET.get('city') or '').strip()

    clients = Clients.objects.select_related('director').all()
    if query_name:
        clients = clients.filter(tszh_name__icontains=query_name)
    if query_inn:
        clients = clients.filter(inn__icontains=query_inn)
    if query_city:
        clients = clients.filter(city__icontains=query_city)

    context = {
        'clients': clients,
        'filters': {
            'name': query_name,
            'inn': query_inn,
            'city': query_city,
        }
    }
    return render(request, 'management/clients_list.html', context)


@staff_required
def client_create(request):
    if request.method == 'POST':
        form = ClientWithDirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clients_list')
    else:
        form = ClientWithDirectorForm()
    return render(request, 'management/client_create.html', {'form': form})


@staff_required
def clients_query_builder(request):
    # Динамический конструктор: пользователь отмечает, какие поля выводить, и фильтры
    # Доступные поля для выбора
    selectable_fields = [
        ("tszh_name", "Название ТСЖ"),
        ("inn", "ИНН"),
        ("city", "Город"),
        ("street_address", "Адрес"),
        ("director__name", "Директор"),
        ("director__phone", "Телефон директора"),
        ("director__email", "Email директора"),
    ]

    selected_fields = request.GET.getlist('fields') or ["tszh_name", "inn", "city"]
    # Фильтры по подстроке
    flt_name = (request.GET.get('flt_name') or '').strip()
    flt_inn = (request.GET.get('flt_inn') or '').strip()
    flt_city = (request.GET.get('flt_city') or '').strip()
    flt_director = (request.GET.get('flt_director') or '').strip()

    qs = Clients.objects.select_related('director').all()
    if flt_name:
        qs = qs.filter(tszh_name__icontains=flt_name)
    if flt_inn:
        qs = qs.filter(inn__icontains=flt_inn)
    if flt_city:
        qs = qs.filter(city__icontains=flt_city)
    if flt_director:
        qs = qs.filter(director__name__icontains=flt_director)

    # Сформировать плоский список значений выбранных полей
    # values() поддерживает двойные подчеркивания для related
    try:
        rows = list(qs.values(*selected_fields))
    except Exception:
        rows = []

    context = {
        'selectable_fields': selectable_fields,
        'selected_fields': selected_fields,
        'filters': {
            'flt_name': flt_name,
            'flt_inn': flt_inn,
            'flt_city': flt_city,
            'flt_director': flt_director,
        },
        'rows': rows,
    }
    return render(request, 'management/clients_query_builder.html', context)


def logout_view(request):
    # Разрешаем выход и по GET, и по POST. Для внутреннего сервиса допустимо,
    # но имейте в виду, что это менее строго с точки зрения CSRF.
    logout(request)
    return redirect('login')
