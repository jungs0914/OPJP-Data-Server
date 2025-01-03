# from abc import ABC, abstractmethod


# class SubscriptionRepository(ABC):
#     @abstractmethod
#     def list(self):
#         pass

#     @abstractmethod
#     def create(self, subsciptionName, subscriptionPrice, subscriptionDescription, subscriptionImage):
#         pass

#     @abstractmethod
#     def findBySubscriptionId(self, subscriptionId):
#         pass

from abc import ABC, abstractmethod
import pandas as pd


class SubscriptionRepository(ABC):

    @abstractmethod
    def create(self, subscriptionData):
        pass

    @abstractmethod
    def findAll(self)-> pd.DataFrame:
        pass

    @abstractmethod
    def save(self, subscriptionData):
        pass