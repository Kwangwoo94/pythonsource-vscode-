# python.org
import requests

with requests.Session() as s:
    r = s.get("http://python.org")
    print(r.text)