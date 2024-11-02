from django.db import models
from base.models import BaseModel

# Create your models here.

class Category(BaseModel):
    category_name = models.CharField(max_length=255)
    # description = models.TextField()
    image = models.ImageField(upload_to="categories")



class Product(BaseModel):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.IntegerField()

class Productimage(BaseModel):
    product = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productimage')