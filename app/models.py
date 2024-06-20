from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Day(models.Model):
    """Model for days of the week"""
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    """Model for expenses"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=3)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.title}"
