# Generated by Django 5.1.5 on 2025-01-30 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_customuser_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="token",
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name="Token"),
        ),
    ]
