# Generated by Django 2.2.24 on 2022-06-27 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220624_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
    ]
