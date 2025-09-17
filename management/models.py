# Файл: web_interface_db/management/models.py
from django.db import models

class Directors(models.Model):
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    tszh_name = models.CharField(max_length=50)
    inn = models.CharField(max_length=20)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=120, blank=True, null=True)
    director = models.OneToOneField(Directors, on_delete=models.SET_NULL, blank=True, null=True)

class InfoTszh(models.Model):
    tszh_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    tszh_name = models.CharField(max_length=100, blank=True, null=True)
    number_1 = models.IntegerField(blank=True, null=True)
    number_1_1 = models.IntegerField(blank=True, null=True)
    tszh_khabarovskaya_66 = models.CharField(max_length=50, blank=True, null=True)

class Echp(models.Model):
    echp_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    copy = models.CharField(max_length=50, blank=True, null=True)
    tszh = models.ForeignKey(InfoTszh, on_delete=models.CASCADE)

class InfoBank(models.Model):
    info_id = models.AutoField(primary_key=True)
    tszh = models.ForeignKey(InfoTszh, on_delete=models.CASCADE)
    name_bank = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class InfoBase(models.Model):
    base_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
