from django.db import models
import uuid


class Ong(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    tel = models.CharField(max_length=15)
    description = models.CharField(max_length=800)
    cnpj = models.CharField(max_length=14, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
