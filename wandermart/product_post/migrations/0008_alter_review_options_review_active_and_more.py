# Generated by Django 5.2 on 2025-05-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_post', '0007_rename_slugpage_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('dateadded',)},
        ),
        migrations.AddField(
            model_name='review',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='review',
            name='dateupdated',
            field=models.DateField(auto_now=True),
        ),
    ]
