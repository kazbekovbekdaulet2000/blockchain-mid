# Generated by Django 3.2.8 on 2021-10-17 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]
