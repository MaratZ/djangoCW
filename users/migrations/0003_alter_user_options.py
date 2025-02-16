from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "permissions": [("can_block_user", "Блокировка пользователя")],
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
    ]
