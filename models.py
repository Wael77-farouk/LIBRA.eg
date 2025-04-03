from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Books(models.Model):
    
    status_books = [
        ('available','available'),
        ('rented','rented'),
        ('sold','sold'),
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=250, null=True , blank=True)
    photo_book = models.ImageField (upload_to='photos' , null=True , blank=True)
    photo_author = models.ImageField (upload_to='photos' , null=True , blank=True)
    pages = models.IntegerField(null=True , blank=True)
    price = models.DecimalField(max_digits=6 , decimal_places=2 , null=True , blank=True)
    retal_price_day = models.DecimalField(max_digits=6 , decimal_places=2 , null=True , blank=True)
    retal_period = models.IntegerField(default=True, null=True , blank=True)
    total_rental = models.DecimalField(max_digits=6 , decimal_places=2 , null=True , default=0)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50 ,  choices=status_books , null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True , blank=True)

    def __str__(self):
        return self.title









