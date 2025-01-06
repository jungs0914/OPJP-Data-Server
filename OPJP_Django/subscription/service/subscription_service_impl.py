# # from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl
# # from subscription.service.subscription_service import SubscriptionService
#
#
# # class SubscriptionServiceImpl(SubscriptionService):
# #     __instance = None
#
# #     def __new__(cls):
# #         if cls.__instance is None:
# #             cls.__instance = super().__new__(cls)
# #             cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()
#
# #         return cls.__instance
#
# #     @classmethod
# #     def getInstance(cls):
# #         if cls.__instance is None:
# #             cls.__instance = cls()
#
# #         return cls.__instance
#
# #     def list(self):
# #         return self.__subscriptionRepository.list()
#
# #     def createSubscription(self, subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
# #         return self.__subscriptionRepository.create(
# #             subscriptionName, subscriptionPrice, subscriptionDescription, subscriptionImage)
#
# #     def readSubscription(self, subscriptionId):
# #         return self.__subscriptionRepository.findBySubscription(subscriptionId)
#
# import os
#
# from subscription.repository.subscription_repository_impl import SubscriptionRepositoryImpl
# from subscription.service.subscription_service import SubscriptionService
#
# import re
# import pandas as pd
#
#
#
# class SubscriptionServiceImpl(SubscriptionService):
#     __instance = None
#
#     def __new__(cls):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#
#             cls.__instance.__subscriptionRepository = SubscriptionRepositoryImpl.getInstance()
#
#         return cls.__instance
#
#     @classmethod
#     def getInstance(cls):
#         if cls.__instance is None:
#             cls.__instance = cls()
#
#         return cls.__instance
#
#     def subscriptionList(self):
#         csvFilePath = os.path.join("resource", "subscription_description_modify.csv")
#
#         # 파일에서 데이터를 읽는 것은 헬퍼로 위임
#         subscriptionDescriptionList = self.__readSubscriptionDescriptionFromFile(csvFilePath)
#         if not subscriptionDescriptionList:
#             return
#
#         print(f"subscriptionDescriptionList: {subscriptionDescriptionList}")
#
#         # 기존 데이터 가져오기
#         existingSubscriptionList = self.__subscriptionRepository.findAll()
#         print(f"existingSubscriptionList: {existingSubscriptionList}")
#
#     # Private Method 1: 파일에서 텍스트 읽기
#     def __readSubscriptionDescriptionFromFile(self, csvFilePath):
#         currentWorkingDirectory = os.getcwd()
#         print(f"현재 작업 디렉터리: {currentWorkingDirectory}")
#
#         # 절대 경로 생성
#         absPath = os.path.join(currentWorkingDirectory, csvFilePath)
#         print(f"absPath: {absPath}")
#
#         if not os.path.exists(absPath):
#             print(f"CSV 파일이 존재하지 않습니다: {absPath}")
#             return None
#
#         try:
#             with open(absPath, newline="", encoding="utf-8") as csvfile:
#                 # 첫 번쨰 줄을 건너뛰고 데이터를 읽어들임
#                 reader = csvfile.readlines()[1:]
#                 return {line.strip() for line in reader if line.strip()}
#         except Exception as e:
#             print(f"CSV 파일을 읽는 중 오류 발생: {e}")
#             return None