
from rest_framework import viewsets
from .models import  Warehouse
from .serializers import WarehouseSerializer
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse




class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by('id_warehouse')
    serializer_class = WarehouseSerializer


    
@require_http_methods(["GET", "HEAD"])
def health_check(request):

    res = JsonResponse({"status": "ok"})
    return _no_store(res)
