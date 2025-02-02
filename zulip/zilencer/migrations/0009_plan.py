# Generated by Django 1.11.11 on 2018-04-12 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0008_customer_billing_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("nickname", models.CharField(max_length=40, unique=True)),
                ("stripe_plan_id", models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
