# Generated by Django 5.1.5 on 2025-01-30 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_customuser_password_change_token"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="password_change_token",
        ),
    ]
