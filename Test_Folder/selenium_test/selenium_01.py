from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('D:/project/face_detecting_project/Test_Folder/selenium_test/chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://naver.com')

search = driver.find_element_by_css_selector('#query')
search.send_keys('드라마 스타트업')
search.send_keys(Keys.ENTER)

actor_tap  = driver.find_element_by_xpath('//*[@id="main_pack"]/div[1]/div[1]/div[4]/div/div/ul/li[5]/a')
actor_tap.click()

thums = driver.find_elements_by_css_selector('.cm_tab_info_box  img')

print("thums : ", len(thums))

for i in thums:
    print(i.get_attribute('src'))

time.sleep(10)
driver.quit()