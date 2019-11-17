from django.contrib import admin

from local.models import Espaco, Locais


class EspacoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'local']


admin.site.register(Locais)
admin.site.register(Espaco, EspacoAdmin)

