import urllib.request as req

# 파일 URL
file_url = "https://img1.daumcdn.net/relay/cafe/original/?fname=http%3A%2F%2Fcfs10.planet.daum.net%2Fupload_control%2Fpcp_download.php%3Ffhandle%3DMzR1Q3FAZnMxMC5wbGFuZXQuZGF1bS5uZXQ6LzEwMDE3NS8wLzAuanBnLnRodW1i%26filename%3D%EA%B0%95%EC%95%84%EC%A7%80.jpg"

# 다음 메인페이지 URL
html_url = "https://www.daum.net/"   # urllib.error.URLError


# 다운로드 받을 경로
save_img = "e:/dog.jpg"
save_html = "e:/daum.html"

try:
    file1, header1 = req.urlretrieve(file_url,save_img)
    file2, header2 = req.urlretrieve(html_url,save_html)
except Exception as e:
    print(e)
else:
    print(header1)
    print(header2)
    print("다운로드 성공")