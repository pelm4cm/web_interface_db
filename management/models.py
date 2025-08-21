# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    client_id = models.AutoField(primary_key=True)
    tszh_name = models.CharField(max_length=50)
    inn = models.CharField(max_length=20)
    city = models.CharField(max_length=50, blank=True, null=True)
    street_address = models.CharField(max_length=120, blank=True, null=True)
    director = models.OneToOneField('Directors', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clients'


class Directors(models.Model):
    director_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directors'


class Echp(models.Model):
    echp_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    copy = models.CharField(max_length=50, blank=True, null=True)
    tszh = models.ForeignKey('InfoTszh', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'echp'


class InfoBank(models.Model):
    info_id = models.AutoField(primary_key=True)
    tszh = models.ForeignKey('InfoTszh', models.DO_NOTHING)
    name_bank = models.CharField(max_length=50, blank=True, null=True)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'info_bank'


class InfoBase(models.Model):
    base_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    client = models.ForeignKey(Clients, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'info_base'


class InfoTszh(models.Model):
    tszh_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Clients, models.DO_NOTHING)
    tszh_name = models.CharField(max_length=100, blank=True, null=True)
    number_1 = models.IntegerField(db_column='1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_1_1 = models.IntegerField(db_column='1_1', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    тсж_хабаровская_66_field = models.CharField(db_column='ТСЖ "Хабаровская 66"', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'info_tszh'
