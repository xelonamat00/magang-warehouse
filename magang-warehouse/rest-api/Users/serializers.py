from rest_framework import serializers
from .models import CustomUserModel
class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['email','name']