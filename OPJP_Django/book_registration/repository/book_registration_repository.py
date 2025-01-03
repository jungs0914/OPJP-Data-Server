from abc import ABC, abstractmethod


class BookRegistrationRepository(ABC):

    @abstractmethod
    def createMany(self, bookRegistrationDate):
        pass

    @abstractmethod
    def findAll(self):
        pass