from django.contrib import admin
from . models import Inventory, Product, Warehouse, Shelve, WarehouseCreation, OrderCreation, AuditLog


admin.site.register(Warehouse)
