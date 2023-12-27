from django.contrib import admin
from apps.base import models
from apps.contacts.models import Contacts,PageContact
# Register your models here.

class ContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'number')
    search_fields = ('name', 'number')


class SettingsPhoneInline(admin.TabularInline):
    model = models.SettingsPhone
    extra = 1

class SettingsFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'descriptions')
    search_fields = ('title', 'descriptions')
    inlines = [SettingsPhoneInline]

class PageContactsFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'number')
    search_fields = ('name', 'number')


admin.site.register(PageContact)
admin.site.register(Contacts, ContactsFilterAdmin)