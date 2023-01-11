# Generated by Django 4.1.4 on 2023-01-09 23:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ongs", "0001_initial"),
        ("donations", "0003_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="ong",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="ong",
            name="users",
            field=models.ManyToManyField(
                related_name="ongs",
                through="donations.Donation",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]