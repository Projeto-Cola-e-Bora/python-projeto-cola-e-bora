# Generated by Django 4.1.4 on 2023-01-05 06:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ongs", "0003_alter_ong_balance"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=127)),
                ("date", models.DateTimeField()),
                ("description", models.TextField()),
                (
                    "ong",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="events",
                        to="ongs.ong",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("street", models.CharField(max_length=127)),
                ("number", models.CharField(max_length=10)),
                ("cep", models.CharField(max_length=10)),
                ("extra", models.CharField(max_length=100)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="events.event",
                    ),
                ),
            ],
        ),
    ]