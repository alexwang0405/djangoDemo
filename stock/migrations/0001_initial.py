# Generated by Django 3.0.3 on 2020-02-15 17:50

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
                ('datetime', models.CharField(max_length=10)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'stock',
            },
        ),
    ]
