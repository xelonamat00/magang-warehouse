from rest_framework import viewsets
from .models import InComingTransact, OutComingTransact
from .serializers import InComingSerializers, OutComingSerializers
# Create your views here.
class OutComingViewSet(viewsets.ModelViewSet):
    # queryset = models.OutComingTransact.objects.select_related('id_item').select_related("user")
    queryset = OutComingTransact.objects.all()
    serializer_class = OutComingSerializers

class InComingViewSet(viewsets.ModelViewSet):
    queryset = InComingTransact.objects.all()
    serializer_class = InComingSerializers