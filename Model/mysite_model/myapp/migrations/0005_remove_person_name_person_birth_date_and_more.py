# Generated by Django 5.1 on 2024-09-26 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_group_manufacturer_topping_remove_person_shirt_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='name',
        ),
        migrations.AddField(
            model_name='person',
            name='birth_date',
            field=models.DateField(default=datetime.date(2000, 1, 1)),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name',
            field=models.CharField(default='John', max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='Witch', max_length=50),
        ),
    ]
