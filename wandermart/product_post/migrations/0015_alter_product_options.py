# Generated by Django 5.2 on 2025-05-18 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_post', '0014_product_avg_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['avg_rating']},
        ),
    ]
