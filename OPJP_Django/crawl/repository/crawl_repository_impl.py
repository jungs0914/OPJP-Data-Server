from crawl.repository.crawl_repository import CrawlReplostiry

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class CrawlRepositoryImpl(CrawlReplostiry):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialize()
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def _initialize(self):
        if not hasattr(self, 'driver'):
            # 크롤링을 위한 Chrome 드라이버 구성
            # self.driver = webdriver.Chrome(ChromeDrivermanager().install())
            self.base_url = "https://"
        
    
    def crawl(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        dataset = []

        for i in range(1, 49):
            if i == 9:
                continue
            try:
                self._navigate_to_book_detail(i)
                book_data = self._extract_book_data()

                dataset.append(book_data)
                self.driver.get(self.base_url)  # 메인 페이지로 돌아가기
                time.sleep(1)

            except Exception as e:
                print(f"Error processing book {i}: {str(e)}")
                continue
        
        self.driver.quit()
        return dataset
    
    # 입력으로 받은 index를 기반으로 도서 모델의 상세 페이지로 이동
    # XPath를 통해 실제 HTML 태그 상의 링크를 찾고 해당 링크로 진입(Keys.ENTER)
    def _navigate_to_book_detail(self, index):
        # //*[@id="container"]에서 id="container"는 웹 브라우저 상의 최상위를 의미
        xpath = f'//*[@id="container]/div/div/div'
        self.driver.find_element(By.XPATH, xpath).send_keys(Keys.ENTER)
        time.sleep(1)
    
    def _extract_book_data(self):
        return {
            "url": self._get_book_url(),
            "bookName": self._get_text(),
            "bookPrice": self._get_text(),
            "bookDescription": self._get_text(),
            "bookImage": self._get_image(),
        }
    
    def _get_book_url(self):
        return self.driver.current_url[22:-4]
    
    def _get_text(self, xpath):
        try:
            return self.driver.find_element(By.XPATH, xpath).text
        except Exception as e:
            print(
                f"Error getting text for xpath {xpath}: {str(e)}"
            )
            return "값 추출 못함"