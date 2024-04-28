from django.contrib import admin
from .models import Kid123, Country123


# Register your models here.


@admin.register(Kid123)
class KidAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Sex', 'Missing_Since', 'Missing_From', 'Nationality', 'Country', 'Height', 'Weight', 'Age']
    list_per_page = 20


@admin.register(Country123)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['country']


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['action_time', 'user', 'content_type', '__str__']
    list_display_links = ['action_time']
    list_filter = ['action_time', 'content_type', 'user']
    list_per_page = 15
    readonly_fields = ['action_time', 'user', 'content_type',
                       'object_id', 'object_repr', 'action_flag', 'change_message']
