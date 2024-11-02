from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='books/')


class bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('user', 'book')


