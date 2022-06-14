from django.contrib import admin
from appFranco.models import familia
# Register your models here.
class familiaresAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellido','edad','profesion','fecha_nacimiento')
admin.site.register(familia, familiaresAdmin)