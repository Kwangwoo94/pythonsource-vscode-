import requests
from bs4 import BeautifulSoup

# 구글 뉴스 사이트에서 파이썬 과 관련된 기사 추출



response = requests.get("https://news.google.com/search?q=파이썬&hl=ko&gl=KR&ceid=KR%3Ako")
soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify())

# 기사 가져오기
articles = soup.find_all("article")
# print(articles)

# 뉴스 타이틀/기사 링크 주소/기사 작성자/기사 작성 시간
for idx, article in enumerate(articles):
    # 뉴스 타이틀과 링크 추출
    title = article.select_one("h3 > a")
    # 작성자
    writer = article.select_one('div a')
    # 작성시간
    date_time = article.select_one("div time")

    # time 태그가 없는 경우가 있음
    if date_time:
        date_time = date_time['datetime']
    else:
        date_time = ""


    print(idx+1)
    print(title.text)
    print(title['href'])
    print(writer.text,date_time)  # date_time.text => 9일전
