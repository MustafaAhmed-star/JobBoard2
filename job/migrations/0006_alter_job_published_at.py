# Generated by Django 4.1.4 on 2022-12-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0005_alter_job_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="published_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]