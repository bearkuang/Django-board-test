from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerilizer):
    class Meta:
        model = Item
        fields = '__all__'