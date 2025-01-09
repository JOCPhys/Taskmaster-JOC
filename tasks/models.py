from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

from django.db import models

# a model for Category to store category names
# category names are unique and no longer than 50 charachters
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# a model for Task to store task title, due date, completion status, and category
# the title is no longer than 100 characters
# completion status is a boolean field with a default value of False
# category is a foreign key to the Category model

class Task(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title