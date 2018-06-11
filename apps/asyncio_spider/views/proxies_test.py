import requests

HEADER = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
PROXIES = {"https": "http://14.118.255.36:6666",}

def fun():
    html = requests.get('http://www.btyunsou.co/search/复仇者_click_1.html', headers=HEADER, proxies=PROXIES).content.decode('utf-8')
    print(html)

fun()