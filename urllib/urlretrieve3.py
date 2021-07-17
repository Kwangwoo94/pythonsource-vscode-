import urllib.request as req

# 좋아하는 연예인 사진 가져오기
url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F112%2F2016%2F09%2F08%2F201609081656205669561_20160908165634_01_99_20160908165707.jpg&type=sc960_832"

save_path = "e:/song.jpg"

try:
    file1, header1 = req.urlretrieve(url,save_path)
except Exception:
    print("다운로드 실패")
else:
    print(header1)
    print("다운로드 성공")