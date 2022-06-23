# Generated by Django 2.2.24 on 2022-06-23 17:17

from django.db import migrations


def fill_new_building_fields(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        if flat.construction_year >= 2015:
            flat.new_building = True
            flat.save()
        else:
            flat.new_building = False
            flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20220623_2000'),
        ('property', '0005_auto_20220623_2016'),
    ]

    operations = [
        migrations.RunPython(fill_new_building_fields)
    ]