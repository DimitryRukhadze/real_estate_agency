# Generated by Django 2.2.24 on 2022-06-27 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20220627_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='compromised_flat',
            new_name='flat',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaint_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='complaint',
            old_name='complaining_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owners_phonenumber',
            new_name='phonenumber',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_pure_phone',
            new_name='pure_phone',
        ),
    ]
