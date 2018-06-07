import asyncio
from bs4 import BeautifulSoup
import requests
import concurrent.futures as cf
import time

HEADER = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
RESULT = []

def spider_btyunsou(i):
    print("job-{} start...".format(i))
    btyunsou_url = 'http://www.btyunsou.co/search/复仇者_click_{}.html'.format(i)
    html = requests.get(btyunsou_url, HEADER).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser').find('ul', class_='media-list media-list-set').find_all('li')
    for item in soup:
        RESULT.append(item)
    print("job-{} finish!!!".format(i))

def spider_77(i):
    print("job-{} start...".format(i))
    search_url = 'http://www.77dht.cn/s/复仇者_type3_page{}.html'.format(i)
    html = requests.get(search_url, HEADER).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser').find('ul', class_='mlist').find_all('li')
    for item in soup:
        RESULT.append(item)
    print("job-{} finish!!!".format(i))

def test():
    print('start 1 th')
    time.sleep(1)
    print('finish 1 th')
    return "1"

def tese02():
    print('start 2 th')
    time.sleep(1)
    print('finish 2 th')
    return None

async def main():
    #启动3个线程
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        loop = asyncio.get_event_loop()
        futures = (
            #新建一个线程来执行耗时函数
            loop.run_in_executor(
                executor,
                spider_77,
            i)
            #fun为需要执行的函数
            for i in range(1, 3)
        )
        #等待执行完成
        result = await asyncio.gather(*futures)
        return result

t1 = time.time()
for i in range(1, 3):
    spider_77(i)
print('spend time:{}s'.format(time.time()-t1))


time.sleep(10)

t2 = time.time()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
result = loop.run_until_complete(main())
print('spend time:{}s'.format(time.time()-t2))
