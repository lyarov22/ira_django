from django.contrib import admin
from .models import Category, Week

class WeekAdmin(admin.ModelAdmin):
    list_display = ('date',)
    list_filter = ('date',)
    date_hierarchy = 'date'

admin.site.register(Week, WeekAdmin)
admin.site.register(Category)
