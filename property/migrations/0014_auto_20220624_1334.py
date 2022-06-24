# Generated by Django 2.2.24 on 2022-06-24 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats_owned',
            field=models.ManyToManyField(blank=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]