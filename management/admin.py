# Файл: web_interface_db/management/admin.py
from django.contrib import admin
from .models import Clients, Directors, Echp, InfoBank, InfoBase, InfoTszh

# Регистрируем каждую модель, чтобы она появилась в админ-панели.
# Для начала просто зарегистрируем их. Позже можно будет добавить кастомные настройки.

admin.site.register(Clients)
admin.site.register(Directors)
admin.site.register(Echp)
admin.site.register(InfoBank)
admin.site.register(InfoBase)
admin.site.register(InfoTszh)
