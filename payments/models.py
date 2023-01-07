from django.db import models
import uuid

class PaymentInfo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    number = models.CharField(max_length=20, unique=True)
    security_code = models.CharField(max_length=3)
    due_date = models.DateField()

    user = models.OneToOneField(
        'users.User',
        on_delete=models.CASCADE,
    )



# Create your models here.
