# Generated by Django 4.2.2 on 2023-06-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0008_rename_service_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
