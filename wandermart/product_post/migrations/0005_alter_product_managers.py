# Generated by Django 5.2 on 2025-05-05 12:14

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_post', '0004_product_publish_alter_product_page'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
