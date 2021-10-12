from rest_framework import serializers
from wise_products.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'quantidade', 'preco']
