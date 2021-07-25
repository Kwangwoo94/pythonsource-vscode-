# 네이버 오픈 api 검색 => 도서

import requests
import pprint
from openpyxl import Workbook
import re


# 엑셀 저장
wb = Workbook()

# 기본 시트 활성화
sheet1 = wb.active

sheet1.title = "베르나르"

# 너비 조절
sheet1.column_dimensions['B'].width = 30   # isbn
sheet1.column_dimensions['C'].width = 100  # title
sheet1.column_dimensions['D'].width = 15   # price
sheet1.column_dimensions['E'].width = 15   # discount

# 제목 행 삽입
sheet1.append(["no","isbn","title","price","discount"])




naver_open_api = "https://openapi.naver.com/v1/search/book.json"
client_id="GRAVYZXY8WQHgZ13OXvV"
client_secret="SQRgIq7tkK"

headers={
    "X-Naver-Client-Id":client_id,
    "X-Naver-Client-Secret":client_secret
}

start,num = 1,1
for idx in range(3):
    start_num = start + (idx*100)  # idx : 0 부터 시작
    param={
        "query":"베르나르 베르베르",
        "start": start_num,
        "display": "100"
    }
    response = requests.get(naver_open_api,headers=headers,params = param)

    data = response.json()
    # pprint.pprint(data)

    for item in data['items']:

        # title 안에 들어있는 태그 제거
        # <b>베르나르 베르베르</b> => <b>, </b>
        title=re.sub("<.*?>","",item['title'])

        print(num, item['isbn'],title,item['price'],item['discount'])
        sheet1.append([num, item['isbn'],title,item['price'],item['discount']])
        num += 1

wb.save("./data/베르나르.xlsx")