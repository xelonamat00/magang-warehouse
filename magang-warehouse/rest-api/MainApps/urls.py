from django.contrib import admin
from django.urls import path, include
from Items.views import ItemViewSet
from Transactions.views import TransactionsViewset
from Users.views import UserViewSet
from rest_framework import routers
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register('item', ItemViewSet)
router.register('transactions', TransactionsViewset)
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', TemplateView.as_view(template_name='index.html')),
]
