# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.response import Response

# from subscription.entity.subscription import Subscription
# from subscription.serializers import SubscriptionSerializer
# from subscription.service.subscription_service_impl import SubscriptionServiceImpl


# # viewsets를 사용하려면 rest_framework가 설정되어야 합니다.
# # pip install djangorestframework
# class SubscriptionView(viewsets.ViewSet):
#     queryset = Subscription.objects.all()
#     subscriptionService = SubscriptionServiceImpl.getInstance()

#     def list(self, request):
#         subscriptionList = self.subscriptionService.list()
#         serializer = SubscriptionSerializer(subscriptionList, many=True)
#         return Response(serializer.data)

#     def register(self, request):
#         try:
#             data = request.data

#             subscriptionImage = request.FILES.get('subscriptionImage')
#             subscriptionName = data.get('subscriptionName')
#             subscriptionPrice = data.get('subscriptionPrice')
#             subscriptionDescription = data.get('subscriptionDescription')

#             if not all([subscriptionImage, subscriptionName, subscriptionPrice, subscriptionDescription]):
#                 return Response({'error': '구독권을 선택해주세요!'}, status=status.HTTP_400_BAD_REQUEST)
            
#             savedSubscription = self.subscriptionService.createSubscription(
#                 subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage
#             )
#             serializer = SubscriptionSerializer(savedSubscription)

#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#         except Exception as e:
#             print('구독 등록 과정 중 문제 발생:', e)
#             return Response({ 'error': str(e)}, status=status.HTTP_400_REQUEST)
    
#     def readSubscription(self, request, pk=None):
#         view_count_subscription_service.increment_subscription_view_count(pk)
#         subscription = self.subscriptionService.readSubscription(pk)
#         serializer = SubscriptionSerializer(subscription)
#         return Response(serializer.data)

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from subscription.service.subscription_service_impl import SubscriptionServiceImpl


class SubscriptionController(viewsets.ViewSet):
    __subscriptionService = SubscriptionServiceImpl.getInstance()

    def requestSubscriptionList(self, request):
        try:
            subscriptionDataFrame = self.__subscriptionService.subscriptionList()
            print(
                f"subscriptionListDataFrame: {subscriptionDataFrame}"
            )
            
            return JsonResponse(
                subscriptionDataFrame.to_dict(orient='records'),
                safe=False,
            )
        except Exception as e:
            return JsonResponse(
                {"error": str(e)}, status = status.HTTP_400_BAD_REQUEST
            )
    
    def requestModifySubscriptionDescription(self, request):
        isSuccess = self.__subscriptionService.requestModifySubscriptionDescription()

        if isSuccess:
            return JsonResponse({ 'success': True})
        else:
            return JsonResponse(
                {'success': False, 'error': 'Failed to modify subscription description'},
                status = status.HTTP_400_BAD_REQUEST,
            )