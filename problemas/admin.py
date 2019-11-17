from django.contrib import admin

from problemas.models import Problema


class ProblemaAdmin(admin.ModelAdmin):
    list_display = ['espaco', 'descricao', 'solucionado']
    list_editable = ('solucionado',)
    list_filter = ('solucionado',)


admin.site.register(Problema, ProblemaAdmin)
