from django.contrib import admin
from django.urls import path, include
from wise_products.views import ProdutosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'produto', ProdutosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
