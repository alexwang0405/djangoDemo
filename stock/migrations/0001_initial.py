# Generated by Django 3.0.3 on 2020-02-29 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('no', models.CharField(max_length=4)),
                ('openprice', models.FloatField()),
                ('endprice', models.FloatField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
