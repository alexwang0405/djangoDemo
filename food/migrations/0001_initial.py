# Generated by Django 3.0.3 on 2020-03-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('datetime', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'food',
            },
        ),
    ]
