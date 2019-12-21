from django.contrib import admin
from django.urls import path, include
from Items.views import ItemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', ItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
