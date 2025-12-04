from rest_framework import serializers
from . import models



class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id_warehouse', 'name', 'location', 'creation_date', 'update_date',)
        model = models.Warehouse
        
