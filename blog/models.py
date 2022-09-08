from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    distance = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=100)
    home = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    cart = models.ImageField(upload_to='images/', blank=True, null=True)
    location_link = models.URLField()
    price = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=100)
    kitchen = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    price = models.CharField(max_length=255)
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Transport(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=255, verbose_name="Цена за одно место")
    place_count = models.IntegerField(verbose_name="Количество мест")
    description = models.TextField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Route(models.Model):
    name = models.CharField(max_length=100)
    transport = models.ForeignKey(Transport, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    transfer_count = models.CharField(verbose_name="Количество пересадок", max_length=255)
    description = models.TextField(max_length=1000)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name