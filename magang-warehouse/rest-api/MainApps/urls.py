from django.contrib import admin
from django.urls import path, include
from Items.views import ItemViewSet
from Transactions.views import OutComingViewSet, InComingViewSet
from Users.views import UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', ItemViewSet)
router.register('out_transactions', OutComingViewSet)
router.register('in_transactions', InComingViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
