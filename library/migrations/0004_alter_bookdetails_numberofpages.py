# Generated by Django 5.0.1 on 2024-01-31 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0003_alter_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookdetails",
            name="NumberOfPages",
            field=models.IntegerField(default=0),
        ),
    ]