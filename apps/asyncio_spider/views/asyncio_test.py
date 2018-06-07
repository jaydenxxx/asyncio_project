import asyncio
import time
import concurrent.futures as cf

# async def job(t):
#     print('Start job ', t)
#     await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
#     print('Job ', t, ' takes ', t, ' s')
#
#
# async def main(loop):                       # async 形式的功能
#     tasks = [
#     loop.create_task(job(t)) for t in range(1, 3)
#     ]                                       # 创建任务, 但是不执行
#     await asyncio.wait(tasks)               # 执行并等待所有任务完成
#
# t1 = time.time()
# loop = asyncio.get_event_loop()             # 建立 loop
# loop.run_until_complete(main(loop))         # 执行 loop
# loop.close()                                # 关闭 loop
# print("Async total time : ", time.time() - t1)

def myfun(i):
    print('start {}th'.format(i))
    time.sleep(1)
    print('finish {}th'.format(i))

async def main():
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        loop = asyncio.get_event_loop()
        futures = (
            loop.run_in_executor(
                executor,
                myfun,
                i)
            for i in range(10)
        )
        for result in await asyncio.gather(*futures):
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())