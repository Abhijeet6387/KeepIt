from django.contrib import admin

# Register your models here.
# To see them in admin panel

from .models import Note

admin.site.register(Note)

