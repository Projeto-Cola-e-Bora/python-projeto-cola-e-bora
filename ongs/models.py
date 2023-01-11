from django.db import models
import uuid

from users.models import User


class OngCategory(models.TextChoices):
    MEIO_AMBIENTE = "meio ambiente"
    ANIMAIS = "animais"
    ASSISTENCIA_SOCIAL = "assistência social"
    CULTURA = "cultura"
    SAUDE = "saúde"
    DESENVOLVIMENTO_DD = "desenvolvimento e defesa de direitos"
    HABITACAO = "habitação"
    EDUCACAO = "educação"
    PESQUISA = "pesquisa"
    OUTRO = "outro"


class Ong(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    tel = models.CharField(max_length=15)
    description = models.CharField(max_length=800)
    cnpj = models.CharField(max_length=14, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    category = models.CharField(
        max_length=40,
        choices=OngCategory.choices,
        default=OngCategory.OUTRO,
    )
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    users = models.ManyToManyField(
        User, through="donations.Donation", related_name="ongs"
    )
