# Generated by Django 4.2.2 on 2023-06-28 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_alter_buyer_purchase_date_alter_seller_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='purchase_date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 8, 57, 37, 617076, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='seller',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 28, 8, 57, 37, 617076, tzinfo=datetime.timezone.utc)),
        ),
    ]