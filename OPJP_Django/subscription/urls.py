# from django.urls import path, include
# from rest_framework.routers import DefaultRouter

# from subscription.controller.subscription_controller import SubscriptionView

# router = DefaultRouter()
# router.register(r'subscription', SubscriptionView)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('list/', SubscriptionView.as_view({'get': 'list'}), name='subscription-list'),
#     path('register/', SubscriptionView.as_view({'post': 'register'}), name='subscription-register'),
#     path('read/<int:pk', SubscriptionView.as_view({'get': 'readSubscription'}), name='subscription-read'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscription.controller.subscription_controller import SubscriptionController

router = DefaultRouter()
router.register(
    r"subscription",
    SubscriptionController,
    basename='subscription'
)

urlpatterns = [
    path('request-subscription-list',
         SubscriptionController.as_view({ 'get': 'requestSubscriptionList'}),
         name='구독권 정보 리스트 획득'),
    path('request-modify-subscription-description',
         SubscriptionController.as_view({ 'get': 'requestModifySubscriptionDescription'}),
         name='구독권 이름 변경'),
]