from django.contrib import admin

from .models import Cliente, Analitica, Categoria_Comida, Comida, Datos_Revision

# Register your models here.


class categoriaComidaViews(admin.ModelAdmin):
    filter_horizontal = ("categorias_comida",)


class platosView(admin.ModelAdmin):
    filter_horizontal = ("platos",)


admin.site.register(Cliente)
admin.site.register(Analitica)
admin.site.register(Categoria_Comida)
admin.site.register(Comida, categoriaComidaViews)
admin.site.register(Datos_Revision)



