# Generated by Django 5.2 on 2025-05-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_productordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='productOrdered',
        ),
        migrations.AddField(
            model_name='order',
            name='orderNum',
            field=models.CharField(default='85113', max_length=150),
        ),
    ]
