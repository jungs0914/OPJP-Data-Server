from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order.controller.order_controller import OrderController

router = DefaultRouter()
router.register(r"order", OrderController, basename='order')

urlpatterns = [
    path('', include(router.urls)),
    path('create',
         OrderController.as_view({ 'post': 'requestCreateOrder'}),
         name='주문 정보 생성'),
    # path('list',
    #      CartController.as_view({ 'post': 'requestListOrder'}),
    #      name='주문 리스트'),
]