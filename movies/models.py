from django.db import models
from django.core.exceptions import ValidationError
import os


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='zmovi_movies', null=True)
    title = models.CharField(max_length=300, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title