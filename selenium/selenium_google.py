from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time
import os 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class google_crowling:

    def __init__(self, ):
        self.SCROLL_PAUSE_SEC = 0.8
        self.url = 'https://www.google.com/search?q='
        self.urlendpoint = '&sxsrf=ALeKk034k-77o9VIlmYURey-dIG0P7a5xg:1608351449580&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjLwM2GmNntAhUCfnAKHWEjAjsQ_AUoAXoECAYQAw&biw=1920&bih=912'
        self.driver = webdriver.Chrome('D:/project/face_detecting_project/Test_Folder/selenium_test/chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.actors = ['배수지', '남주혁']
        self.save_path = {
        '배수지' : 'D:/project/face_detecting_project/image_data/origin_data/su/',
        '남주혁' : 'D:/project/face_detecting_project/image_data/origin_data/nam/'
        }

    def start(self):
        driver = self.driver
        actors = self.actors
        url = self.url
        url_end = self.urlendpoint
        for i in range(len(actors)):
            image_page = driver.get(url + actors[i]+url_end)
            time.sleep(0.5)

            self.scroll_dowon(driver, actors[i])


    def scroll_dowon(self, driver, actor):
        # 스크롤 전체 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(self.SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 전체  높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            more = driver.find_element_by_css_selector('.YstHxe')
            print(more.get_attribute('style'))


            if not('display: none;' in more.get_attribute('style')):
                more.click()
                time.sleep(1)
                last_height = new_height
                continue

                
    
            
            # 전체 높이가 변하지 않았다면 끝! 변했다면 데이터가 더 존재 
            if new_height == last_height :
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1.5)
                self.src_download(driver, actor)

                break

            time.sleep(1)
            last_height = new_height

    def src_download(self, driver, actor):
        save_path = self.save_path
        img_list = driver.find_elements_by_css_selector('.bRMDJf img')
        count = len(os.listdir( save_path[actor]))
        print(count)
        for img in img_list:
            try:
                img.click()
                time.sleep(1.5)
                img_sorce = driver.find_element_by_css_selector('.v4dQwb img')
                urlretrieve(img_sorce.get_attribute('src'), save_path[actor]+str(count)+'.png')
                count +=1
            except:
                continue
if __name__ == '__main__':

    google = google_crowling()
    google.start()
