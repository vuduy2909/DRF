# Generated by Django 5.1 on 2024-09-26 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_place_address_alter_place_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPerson',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.person',),
        ),
    ]
