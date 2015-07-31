# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()


#Person.objects.get_or_create(name='online',number=3)
#Person.objects.create(name='online', number=2)

#p = Person(name='sended', number=23)
#p.save()

# Create your models here.


class EndDataPool(models.Model):
    sockfd = models.CharField(max_length=15, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    mac_address = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    product_id = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=32, blank=True, null=True)
    kernel_version = models.CharField(max_length=32, blank=True, null=True)
    cpu_model = models.CharField(max_length=64, blank=True, null=True)
    bios_version = models.CharField(max_length=16, blank=True, null=True)
    graphics_model = models.CharField(max_length=128, blank=True, null=True)
    graphics_driver_version = models.CharField(max_length=32, blank=True, null=True)
    client_version = models.CharField(max_length=8, blank=True, null=True)
    online_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end_data_pool'


class EndRawData(models.Model):
    ip = models.CharField(max_length=15, blank=True, null=True)
    sockfd = models.CharField(max_length=15, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    used_status = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'end_raw_data'


class PushDataPool(models.Model):
    raw_data = models.ForeignKey('PushRawData', blank=True, null=True)
    muid = models.CharField(max_length=8)
    packed_message = models.TextField()
    sent_status = models.IntegerField(blank=True, null=True)
    sent_number = models.IntegerField(blank=True, null=True)
    recv_number = models.IntegerField(blank=True, null=True)
    open_number = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_data_pool'


class PushRawData(models.Model):
    raw_message = models.TextField()
    raw_url = models.TextField(blank=True, null=True)
    used_status = models.IntegerField()
    send_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_raw_data'


class ShowEndAlive(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.CharField(unique=True, max_length=32, blank=True, null=True)
    mac_address = models.CharField(max_length=32, blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    product_id = models.CharField(max_length=32, blank=True, null=True)
    os_version = models.CharField(max_length=32, blank=True, null=True)
    kernel_version = models.CharField(max_length=32, blank=True, null=True)
    cpu_model = models.CharField(max_length=64, blank=True, null=True)
    bios_version = models.CharField(max_length=16)
    graphics_model = models.CharField(max_length=128, blank=True, null=True)
    graphics_driver_version = models.CharField(max_length=32, blank=True, null=True)
    client_version = models.CharField(max_length=8, blank=True, null=True)
    online_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show_end_alive'
        unique_together = (('id', 'bios_version'),)


class ShowPushMessage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    raw_data_id = models.IntegerField(blank=True, null=True)
    sent_message = models.TextField()
    sent_url = models.TextField(blank=True, null=True)
    sent_number = models.IntegerField(blank=True, null=True)
    recv_number = models.IntegerField(blank=True, null=True)
    open_number = models.IntegerField(blank=True, null=True)
    sent_time = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'show_push_message'

