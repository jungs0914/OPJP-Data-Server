from abc import ABC, abstractmethod


class CrawlReplostiry(ABC):

    @abstractmethod
    def crawl(self):
        pass