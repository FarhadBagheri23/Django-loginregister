from django.db import models
from acc.models import CustomUser

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length = 32)
    members = models.ManyToManyField(CustomUser)

class Expense(models.Model):
    title = models.CharField(max_length = 32)
    description = models.TextField()
    amount = models.DecimalField(max_digits = 11, decimal_places = 2)
    group = models.ForeignKey(Group, on_delete = models.CASCADE, related_name='group')
    paid_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="payer")



