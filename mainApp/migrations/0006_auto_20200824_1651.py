# Generated by Django 3.0.9 on 2020-08-24 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_product_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
