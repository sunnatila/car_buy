from django.db import models


class Cars(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=50)
    car_color = models.CharField(max_length=50, verbose_name='Mashinaning rangi')
    car_create_day = models.CharField(max_length=50, verbose_name='Mashinaning yili')
    car_price = models.IntegerField(verbose_name='Mashinaning narxi')
    car_active = models.BooleanField(default=True, verbose_name='Mashina sotiladimi')

    def __str__(self):
        return self.car_model

    objects = models.Model



