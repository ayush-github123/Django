from django.db import models

# Create your models here.
CATEGORY_CHOICES = [
    ('appetizer','Appetizer'),
    ('main_course','Main Course'),
    ('dessert','Dessert')
]
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name             #added to view recipe_name is admin/shell instead of object1 or object2, etc
    
