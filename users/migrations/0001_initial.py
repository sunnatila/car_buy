# Generated by Django 5.0.6 on 2024-07-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=50)),
                ('car_model', models.CharField(max_length=50)),
                ('car_color', models.CharField(max_length=50, verbose_name='Mashinaning rangi')),
                ('car_create_day', models.CharField(max_length=50, verbose_name='Mashinaning yili')),
                ('car_price', models.IntegerField(verbose_name='Mashinaning narxi')),
                ('car_active', models.BooleanField(default=True, verbose_name='Mashina sotiladimi')),
            ],
        ),
    ]
