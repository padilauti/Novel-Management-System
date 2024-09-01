from django.contrib import admin

# Register your models here.
from .models import Novel

class NovelAdmin(admin.ModelAdmin):
    readonly_fields=[
        'slug',
        'updated',
        'published',
    ]
admin.site.register(Novel, NovelAdmin)