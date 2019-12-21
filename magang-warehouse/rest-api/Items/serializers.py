from .models import Item
from rest_framework import serializers

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        # fields = ['url','id_item','name','brand','quantity','unit','description','category','classes','size']
        fields = '__all__'