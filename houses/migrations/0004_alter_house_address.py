# Generated by Django 4.2 on 2023-04-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_alter_house_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.CharField(blank=True, max_length=255, unique=True),
        ),
    ]