from selenium import webdriver

driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)

# 접속할 사이트
driver.get("https://www.daum.net")

print("session id ",driver.session_id)
print("title ",driver.title)
print("url ",driver.current_url)
print("cookies ",driver.get_cookies)
print(driver.page_source)




driver.close()