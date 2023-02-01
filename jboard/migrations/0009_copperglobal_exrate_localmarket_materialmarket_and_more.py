# Generated by Django 4.1.2 on 2023-02-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jboard", "0008_alter_pfkstocks_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="CopperGlobal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("lastvalue", models.FloatField()),
                ("difference", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="ExRate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("lastvalue", models.FloatField()),
                ("difference", models.FloatField()),
                ("Curr_Type", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="LocalMarket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("lastvalue", models.FloatField()),
                ("difference", models.FloatField()),
                ("diffrate", models.FloatField()),
                ("startvalue", models.FloatField()),
                ("highvalue", models.FloatField()),
                ("lowvalue", models.FloatField()),
                ("volume", models.FloatField()),
                ("tranaction", models.BigIntegerField()),
                ("marketcap", models.BigIntegerField()),
                ("market_type", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="MaterialMarket",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("lastvalue", models.FloatField()),
                ("difference", models.FloatField()),
                ("market_type", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="PFExrate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("curr_type", models.IntegerField()),
                ("buyprice", models.IntegerField()),
                ("buynum", models.IntegerField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="PFUSStocks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=30)),
                ("buyprice", models.IntegerField()),
                ("buynum", models.IntegerField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name="pfbonds",
            name="code",
            field=models.CharField(max_length=30),
        ),
    ]
