# Generated by Django 4.1.7 on 2023-02-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
