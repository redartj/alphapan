# Generated by Django 4.1.2 on 2023-01-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jboard", "0007_pfbonds_pfkstocks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pfkstocks",
            name="code",
            field=models.CharField(max_length=30),
        ),
    ]
