from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Buyer)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'description',)
    # fields = [('title', 'description',)]
    search_fields = ('title',)
    list_filter = ('cost',)
    fieldsets = (
        ('info, ', {
            'fields':
                ('title', 'cost',)
        }),
        ('footer', {
            'fields':
                ('description',)
        })

    )
