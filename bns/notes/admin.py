from django.contrib import admin

# Register your models here.
from .models import Contact, AllNotes

admin.site.register(Contact)
admin.site.register(AllNotes)