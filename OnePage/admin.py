from django.contrib import admin
from .models import Contact


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']  # here Message is not written as it is to big to display in one line
    list_filter = ['name']
    search_fields = ['name', 'subject']

