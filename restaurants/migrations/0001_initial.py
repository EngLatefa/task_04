# Generated by Django 2.0.4 on 2018-11-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restuaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('description', models.TextField()),
                ('opening_time', models.TimeField(auto_now_add=True)),
                ('closing_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
