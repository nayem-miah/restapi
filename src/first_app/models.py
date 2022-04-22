from datetime import date, time
from django.db import models
from datetime import datetime
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields.files import ImageField
from django.utils.timezone import now
from PIL import Image
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    text = models.TextField()
    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=200)
    biodata = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    image = models.ImageField(upload_to='realtor')
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name


class Home(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
    class HomeType(models.TextChoices):
        HOUSE = 'House'
        FLAT = 'Flat'
    agent = models.ForeignKey(Agent, on_delete= DO_NOTHING, related_name='agents')
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zipcode=models.CharField(max_length=150)
    description=models.TextField()
    sale_type=models.CharField(max_length=50, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=50, choices=HomeType.choices,default=HomeType.HOUSE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to = 'home', blank=True)
    list_date = models.DateTimeField(default=now,blank=True)
    def __str__(self):
        return self.slug

class Image_files(models.Model):
    image = models.ImageField(upload_to = "home")
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='images')
    #this save method here used not to have big image
    def save(self, *args, **kwargs):
        super(Image_files, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




