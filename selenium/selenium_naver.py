from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time
import os 

class naver_crowling:

    def __init__(self, ):
        self.SCROLL_PAUSE_SEC = 0.8
        self.url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
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
        for i in range(len(actors)):
            image_page = driver.get(url + actors[i])
            time.sleep(0.5)

            self.scroll_dowon(driver, actors[i])

        time.sleep(10)
        driver.quit()

    def scroll_dowon(self, driver, actor):
        # 스크롤 전체 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(self.SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 전체  높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            #다음버튼
            more = driver.find_element_by_css_selector('.btn_more')

            if more.get_attribute('style') == '':
                more.click()
            
            # 전체 높이가 변하지 않았다면 끝! 변했다면 데이터가 더 존재 
            if new_height == last_height :
                self.src_download(driver, actor)
                time.sleep(10)
                driver.quit()
                break

            last_height = new_height

    def src_download(self, driver, actor):
        save_path = self.save_path
        img_list = driver.find_elements_by_css_selector('.img_area')
        count = len(os.listdir( save_path[actor]))
        print(count)
        for img in img_list:
            img.click()
            img_sorce = driver.find_element_by_css_selector('._image_source')
            urlretrieve(img_sorce.get_attribute('src'), save_path[actor]+str(count)+'.png')
            time.sleep(0.5)
            count +=1

if __name__ == '__main__':

    naver = naver_crowling()
    naver.start()
