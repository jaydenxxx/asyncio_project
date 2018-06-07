import asyncio
import time

async def job(t):
    print("Start job {}".format(t))
    await asyncio.sleep(t)
    print("Job", t ,"takes", t, "s")

async def main(loop):
    tasks = [
        loop.create_task(job(t) for t in range(1,10))
    ]
    await asyncio.wait(tasks)

