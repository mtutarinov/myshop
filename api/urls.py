from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
# router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderitem', OrderItemViewSet)

app_name = 'api'
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls)),
    path('v1/', include(router.urls)),
]
