# Generated by Django 4.1.4 on 2022-12-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0005_remove_profile_image_profile_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(default=1, upload_to="accounts\\profile"),
            preserve_default=False,
        ),
    ]
