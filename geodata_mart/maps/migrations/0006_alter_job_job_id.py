# Generated by Django 3.2.13 on 2022-07-07 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_auto_20220706_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_id',
            field=models.CharField(default='f93f5ca3fb7549e192ca4b3a2c8215f7', max_length=32, unique=True, verbose_name='Job ID'),
        ),
    ]
