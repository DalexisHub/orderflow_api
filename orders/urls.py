from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]