from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventories.views import WarehouseViewSet, health_check


router = DefaultRouter()
router.register(r"warehouses", WarehouseViewSet, basename="warehouse")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),  # /api/products/ endpoints
    path("health-check/", health_check),  # /health-check/ endpoints
]
