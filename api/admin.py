from django.contrib import admin

# Register your models here.
from .models import Note
from django.contrib.sessions.models import Session

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "body")

admin.site.register(Note, NoteAdmin)
admin.site.register(Session)