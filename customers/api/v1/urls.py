from django.urls import include, path
from rest_framework import routers

from customers.api.v1.views import CustomerViewSet, ProductViewSet

router = routers.SimpleRouter()
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [
    path('v1/', include(router.urls)),
]
