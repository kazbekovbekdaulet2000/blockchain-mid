# Generated by Django 3.2 on 2021-10-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_auto_20211014_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'На комплектации'), (1, 'В пути'), (2, 'Доставлен')], default=0),
        ),
    ]
