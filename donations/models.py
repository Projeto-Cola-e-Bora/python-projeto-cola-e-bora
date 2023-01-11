from django.db import models
from users.models import User
from ongs.models import Ong
import uuid


class Donation(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
