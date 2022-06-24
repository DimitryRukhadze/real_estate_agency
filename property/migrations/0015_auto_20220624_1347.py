# Generated by Django 2.2.24 on 2022-06-24 10:47

from django.db import migrations


def make_owner_from_flat_details(apps, schema_editor):
    Owner = apps.get_model('property', 'Owner')
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        new_owner = Owner.objects.get_or_create(
            owner=flat.owner,
            defaults={
                'owners_phonenumber': flat.owners_phonenumber,
                'owner_pure_phone': flat.owner_pure_phone
            }
        )


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20220624_1334'),
    ]

    operations = [
        migrations.RunPython(make_owner_from_flat_details)
    ]
