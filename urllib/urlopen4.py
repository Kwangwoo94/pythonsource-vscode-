import urllib.request as req

# urlopen : 메모리에 내용을 올려놓고 분석

# 파일 URL
file_url = ["https://www.daum.net/",
"https://img1.daumcdn.net/relay/cafe/original/?fname=http%3A%2F%2Fcfs10.planet.daum.net%2Fupload_control%2Fpcp_download.php%3Ffhandle%3DMzR1Q3FAZnMxMC5wbGFuZXQuZGF1bS5uZXQ6LzEwMDE3NS8wLzAuanBnLnRodW1i%26filename%3D%EA%B0%95%EC%95%84%EC%A7%80.jpg"]

# 저장할 경로 지정
path_list = ["e:/daum1.html","e:/dog1.jpg"]

for i, url in enumerate(file_url):

    try:
        response = req.urlopen(url)
        contents = response.read()

        # 파일저장 (wb-write byte)
        with open(path_list[i],"wb") as c:
            c.write(contents)

    except:
        print("에러발생")
    else:      
        print("headers info-{}:{}".format(i, response.info())) 
        print()
        print("---------------------------------------")

        print(contents.decode("utf-8")[:3000])


