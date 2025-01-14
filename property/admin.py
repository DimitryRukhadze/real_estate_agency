from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnerInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ['owner']

@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    list_display = [
        'address',
        'price',
        'new_building',
        'construction_year',
        'town'
    ]
    list_editable = ['new_building']
    readonly_fields = ['created_at']
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'active']
    raw_id_fields = ['liked_by']
    inlines = [
        FlatOwnerInline,
    ]

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['user', 'flat']

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats_owned']
