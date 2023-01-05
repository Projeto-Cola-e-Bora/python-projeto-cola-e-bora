from django.db import models
import uuid


class Event(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=127)
    date = models.DateTimeField()
    description = models.TextField()

    address = models.ForeignKey(
        "addresses.Address",
        related_name="event",
        on_delete=models.CASCADE,
    )

    ong = models.ForeignKey("ongs.Ong", on_delete=models.CASCADE, related_name="events")
