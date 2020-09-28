from django.db import models


# Create your models here.

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    first_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    

class Item_Details(models.Model):

    item_id = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    link = models.CharField(max_length=255, null=True)  # link to items detail page
    title = models.CharField(max_length=255, null=True)  # descriptive title
    pic = models.URLField(max_length=255, null=True)  # descriptive title
    category = models.CharField(max_length=255, null=True)  # Haus, Mittelreihenhaus, ...
    obj_cat = models.CharField(max_length=30, null=True)  # Stadthaus
    marketingtype = models.CharField(max_length=255, null=True)  # Kauf
    price = models.IntegerField(null=True)
    fed = models.CharField(max_length=50, null=True)  # S-H
    city = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=5, null=True)
    area = models.PositiveSmallIntegerField(null=True)  # m²
    areaeffective = models.PositiveSmallIntegerField(null=True)  # Grundstück m²
    rooms = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    first_occupancy = models.CharField(max_length=255, null=True)  # Erstbezug ja/nein
    balcony = models.BooleanField(null=True)
    garden = models.BooleanField(null=True)
    kitchen = models.BooleanField(null=True)
    description = models.TextField(null=True)
