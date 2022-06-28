# Generated by Django 2.2.24 on 2022-06-24 09:32
import phonenumbers
from django.db import migrations


def copy_parsed_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number):
            flat.owner_pure_phone = parsed_number
            flat.save()

def reverse_changes(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all().iterator():
        flat.owner_pure_phone = ''
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(copy_parsed_phonenumbers, reverse_changes)
    ]
