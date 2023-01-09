from django.db import models
import uuid
from django.core.exceptions import ValidationError
import datetime
from datetime import timezone, timedelta
from .errors import ValidationDateError


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
    volunteers = models.ManyToManyField(
        "users.User", through="events.EventVolunteers", related_name="event_volunteers"
    )

    def save(self, *args, **kwargs):
        tz_offset = -8.0
        tzinfo = timezone(timedelta(hours=tz_offset))
        if self.date < datetime.datetime.now(tzinfo):
            raise ValidationDateError("The event date cannot be a past date")
        super(Event, self).save(*args, **kwargs)


class EventVolunteers(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    event = models.ForeignKey(
        "events.Event", on_delete=models.CASCADE, related_name="event_users_events"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_events"
    )
    

