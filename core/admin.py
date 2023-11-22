from django.contrib import admin

from core.models import Ordem, SeuModelo, Celular, Console

admin.site.register(Ordem)
admin.site.register(SeuModelo)
admin.site.register(Celular)
admin.site.register(Console)