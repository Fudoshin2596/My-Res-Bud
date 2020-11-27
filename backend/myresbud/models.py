from django.db import models
from django.contrib.auth import get_user_model
from django_google_maps.fields import AddressField
from phonenumber_field.modelfields import PhoneNumberField

class Resturant(models.Model):
    name = models.CharField(max_length=100)
    address = AddressField(max_length=100)
    notes = models.TextField(max_length=5000, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=255)
    phone_number = PhoneNumberField()
    website = models.URLField(blank=True, null=True)
    slug = models.SlugField(
                max_length=50, null=True, blank =True, unique=True)
    posted_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.address}; {self.price} | {self.rating}'
