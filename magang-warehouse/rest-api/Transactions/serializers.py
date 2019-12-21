from . import models
from rest_framework import serializers
from Items.serializers import ItemSerializers
from Users.serializers import UserSerializers

class InComingSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.InComingTransact
        fields = ['url','no_transac','sender','id_item','user']

class OutComingSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.OutComingTransact
        fields = ['url','no_transac','date','recipient','id_item','user']

    