# Generated by Django 4.1.4 on 2022-12-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("job", "0008_job_experience_job_salary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(max_length=500, null=True),
        ),
    ]
