from django.contrib import admin

from core.models import Ordem, SeuModelo, Celular, Console, Desktop, Notebook

admin.site.register(Ordem)
admin.site.register(SeuModelo)
admin.site.register(Celular)
admin.site.register(Console)
admin.site.register(Desktop)
admin.site.register(Notebook)