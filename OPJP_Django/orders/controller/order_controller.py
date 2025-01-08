from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl
# from orders.service.order_service_impl import OrderServiceImpl
# Create your views here.


class OrderController(viewsets.ViewSet):
    redisCacheService = RedisCacheServiceImpl.getInstance()
    # orderService = OrderServiceImpl.getInstance()

    def requestCreateOrder(self, request):
        postRequest = request.data
        cart = postRequest.get("cart")
        userToken = postRequest.get("userToken")

        if not userToken:
            return JsonResponse(
                {"error": "userToken이 필요합니다.", "success": False},
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)

            # updatedCart = self.orderService.createOrder(accountId, cart)
            # if updatedCart is not None:
            #     return JsonResponse(
            #         {"message": "주문이 완료 되었습니다.", "success": True},
            #         status = status.HTTP_200_OK,
            #     )
        
        except Exception as e:
            print(f"주문 처리 중 오류 발생: {e}")
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )