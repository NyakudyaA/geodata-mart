# Generated by Django 3.2.13 on 2022-07-27 20:03

import django.core.files.storage
from django.db import migrations
import geodata_mart.vendors.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='logo',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/geodata/assets', location='/qgis'), upload_to=geodata_mart.vendors.models.Vendor.getVendorUploadPath, verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='media',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/geodata/assets', location='/qgis'), upload_to=geodata_mart.vendors.models.Vendor.getVendorUploadPath, verbose_name='Media'),
        ),
    ]
