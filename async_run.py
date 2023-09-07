import asyncio
import aiohttp
import logging as log
log.basicConfig(format='%(asctime)s %(message)s', level=log.DEBUG)


async def fetcher(times: int):
    log.info(f"第{times}条任务开始...")
    async with aiohttp.ClientSession() as session:
        resp = await session.get("http://127.0.0.1:8000/api/config/getAllFolders")
        log.info("请求已发送...")
        log.info(await resp.text())
    log.info(f"第{times}条任务结束...")
    return "Success"


async def main():
    # raise NotImplementedError
    results = await asyncio.gather(*(fetcher(times) for times in range(10)))
    for ret in results:
        print(ret)


if __name__ == "__main__":
    asyncio.run(main())
