from django.db import models

class Abilities(models.Model):
    class_name = models.CharField(max_length=100, blank=True)
    short_description = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = 'Abilities'
        verbose_name = 'Ability'

    def __str__(self):
        return self.short_description

class Clients(models.Model):
    image = models.ImageField(upload_to='pictures')
    living_adress = models.CharField(max_length=100)
    feedback = models.TextField(max_length=250)

    class Meta:
        verbose_name_plural = 'Clients'
        verbose_name = 'Client'

    def __str__(self):
        return self.living_adress

class Prices(models.Model):
    breed = models.CharField(max_length=50)
    price = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = 'Prices'
        verbose_name = 'Price'

    def __str__(self):
        return self.breed
