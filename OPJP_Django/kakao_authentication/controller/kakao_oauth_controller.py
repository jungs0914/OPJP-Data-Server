# import uuid

# from django.db import transaction
# from django.http import JsonResponse
# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.status import HTTP_200_OK

# from kakao_account.service.account_service_impl import AccountServiceImpl
# from kakao_account_profile.service.account_profile_service_impl import AccountProfileServiceImpl
# from kakao_authentication.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
# from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl
# from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


# class KakaoOauthcontroller(viewsets.ViewSet):
#     kakaoOauthService = KakaoOauthServiceImpl.getInstance()
#     accountService = AccountServiceImpl.getInstance()
#     accountProfileService = AccountProfileServiceImpl.getInstance()
#     redisCacheService = RedisCacheServiceImpl.getInstance()

#     def requestKakaoOauthLink(self, request):
#         url = self.kakaoOauthService.requestKakaoOauthLink()

#         return JsonResponse({"url": url}, status=status.HTTP_200_OK)
    
#     def requestAccessToken(self, request):
#         serializer = KakaoOauthAccessTokenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         code = serializer.validated_data['code']

#         try:
#             tokenResponse = self.kakaoOauthService.requestAccessToken(code)
#             accessToken = tokenResponse['access_token']

#             with transaction.atomic():
#                 userInfo = self.kakaoOauthService.requestUserInfo(accessToken)
#                 nickname = userInfo.get('properties', {}).get('nickname', '')
#                 email = userInfo.get('kakao_account', {}).get('email', '')

#                 createdAccount = self.accountService.createAccount(email)
#                 createdAccountProfile = self.accountProfileService.createAccountProfile(
#                     createdAccount.getId(), nickname
#                 )

#                 userToken = self.__createUserTokenWithAccessToken(createdAccount, accessToken)
            
#             return JsonResponse({'userToken': userToken})
        
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
    
#     def __createUserTokenWithAccessToken(self, account, accessToken):
#         try:
#             userToken = str(uuid.uuid4())
#             self.redisCacheService.storeKeyValue(account.getId(), accessToken)
#             self.redisCacheService.storeKeyValue(userToken, account.getId())

#             return userToken
        
#         except Exception as e:
#             print('Redis에 토큰 저장 중 에러:', e)
#             raise RuntimeError('Redis에 토큰 저장 중 에러')

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl



class AuthenticationController(viewsets.ViewSet):
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestLogout(self, request):
        postRequest = request.data
        userToken = postRequest.get("userToken")

        if userToken:
            try:
                accountId = self.redisCacheService.getValueByKey(userToken)
                self.redisCacheService.deleteKey(userToken)
                self.redisCacheService.deleteKey(accountId)
                return JsonResponse(
                    {"message": "로그 아웃 성공"},
                    status = status.HTTP_200_OK,
                )
            
            except Exception as e:
                print(f"redis key 삭제 중 에러 발생: {e}")
                return JsonResponse(
                    {"error": "코드 내부 에러"},
                    status = status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        
        return JsonResponse(
            {"error": "userToken이 필요합니다."},
            status = status.HTTP_400_BAD_REQUEST,
        )
    
    def requestUserTokenValidation(self, request):
        postRequest = request.data
        userToken = postRequest.get("userToken")

        if not userToken:
            return JsonResponse(
                {"valid": False, "error": "userToken이 필요합니다."},
                status = status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            accountId = self.redisCacheService.getValueByKey(userToken)
            if not accountId:
                return JsonResponse(
                    {"valid": False},
                    status = status.HTTP_200_OK,
                )
            return JsonResponse(
                {"valid": True},
                status = status.HTTP_200_OK,
            )
        
        except Exception as e:
            return JsonResponse(
                {"valid": False, "error": "코드 내부 에러"},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR,
            )