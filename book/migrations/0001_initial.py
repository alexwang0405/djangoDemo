# Generated by Django 3.0.3 on 2020-03-10 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=6)),
                ('link', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]