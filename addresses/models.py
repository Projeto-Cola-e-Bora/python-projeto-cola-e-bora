from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    street = models.CharField(max_length=127)
    number = models.CharField(max_length=10)
    cep = models.CharField(max_length=10)
    extra = models.CharField(max_length=100)
