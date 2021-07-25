import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

userAgent = UserAgent()
headers = {
    "user-agent":userAgent.chrome
}


url = "https://news.naver.com/main/read.naver?mode=LSD&mid=shm&sid1=102&oid=437&aid=0000271006"

response = requests.get(url,headers=headers)
#print(response.text)

# 필요 데이터 추출 => BeautifulSoup
soup = BeautifulSoup(response.text,'html.parser')

# find('h3',....) : 가장 처음에 만나는 태그 찾아주기
title = soup.find('h3',id="articleTitle")
print(title)
print(title.string)
print(title.get_text())

