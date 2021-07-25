from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome("./driver/chromedriver")

driver.get("https://www.daum.net")

# 검색 창에 검색어를 넣고 결과 페이지 받기
# find_~~~() : 원하는 요소 찾기

# 검색 창 요소 찾기
# <selenium.webdriver.remote.webelement.WebElement (session="4d86381399585d22e339169b2c85e8b4", element="cb683303-40d6-41b7-a8d0-8db69b02ab64")>
element = driver.find_element(By.NAME, "q")

# 검색어 넣기
element.send_keys("안드로이드")
# 엔터 넣기
element.send_keys(Keys.RETURN)


time.sleep(3)

driver.close()