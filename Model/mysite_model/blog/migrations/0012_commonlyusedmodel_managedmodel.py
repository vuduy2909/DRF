# Generated by Django 5.1 on 2024-09-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_restaurant'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonlyUsedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'app_largetable',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManagedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f1', models.CharField(max_length=10)),
                ('f2', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'app_largetable',
            },
        ),
    ]
