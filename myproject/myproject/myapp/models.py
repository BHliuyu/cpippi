# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cpi(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    cpi_true = models.FloatField(blank=True, null=True)
    cpi_forecast = models.FloatField(blank=True, null=True)
    cpi_market_forecast = models.FloatField(blank=True, null=True)
    cpi_tail = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpi'


class CpiHighFreqData(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    allcountry = models.FloatField(blank=True, null=True)
    thirtythreecitysale = models.FloatField(blank=True, null=True)
    twentytwocitysale = models.FloatField(blank=True, null=True)
    twentyeightvegetables = models.FloatField(blank=True, null=True)
    sevenfruits = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpi_high_freq_data'


class CpiMom(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    cpi_true = models.FloatField(blank=True, null=True)
    cpi_forecast = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cpi_mom'


class Cpicompare(models.Model):
    level = models.CharField(max_length=255, primary_key=True)
    our_number = models.IntegerField()
    other_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cpicompare'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ppi(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    ppi_true = models.FloatField(blank=True, null=True)
    ppi_forecast = models.FloatField(blank=True, null=True)
    ppi_market_forecast = models.FloatField(blank=True, null=True)
    ppi_tail = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppi'


class PpiHighFreqData(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    crudeoil = models.FloatField(blank=True, null=True)
    hrb400 = models.FloatField(blank=True, null=True)
    lmecopper = models.FloatField(blank=True, null=True)
    myipicindexmine = models.FloatField(blank=True, null=True)
    gasoline = models.FloatField(blank=True, null=True)
    dieselfuel = models.FloatField(blank=True, null=True)
    urea = models.FloatField(blank=True, null=True)
    steel = models.FloatField(blank=True, null=True)
    po = models.FloatField(blank=True, null=True)
    pta = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppi_high_freq_data'


class PpiMom(models.Model):
    date = models.DateField(blank=True, primary_key=True)
    ppi_true = models.FloatField(blank=True, null=True)
    ppi_forecast = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ppi_mom'


class Ppicompare(models.Model):
    level = models.CharField(max_length=255, primary_key=True)
    our_number = models.IntegerField()
    other_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ppicompare'
