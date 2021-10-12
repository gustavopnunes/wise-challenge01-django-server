from django.contrib import admin
from wise_products.models import Produto


class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'quantidade', 'preco')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Produto, Produtos)