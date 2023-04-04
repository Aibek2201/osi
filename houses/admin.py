from django.contrib import admin

from . import models


class HouseAdmin(admin.ModelAdmin):
    list_display = ('street', 'number')


admin.site.register(models.House, HouseAdmin)
