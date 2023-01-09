# Generated by Django 4.1.4 on 2023-01-05 13:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("donations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]