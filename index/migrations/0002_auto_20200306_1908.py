# Generated by Django 3.0.3 on 2020-03-06 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Index',
            new_name='Home',
        ),
        migrations.AlterModelTable(
            name='home',
            table='home',
        ),
    ]