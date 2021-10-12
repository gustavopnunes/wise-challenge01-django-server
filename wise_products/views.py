from rest_framework import viewsets
from wise_products.models import Produto
from wise_products.serializer import ProdutoSerializer


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
