# Generated by Django 3.0.3 on 2020-03-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'index',
            },
        ),
    ]
