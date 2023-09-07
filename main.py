import asyncio
import time
import sys
import logging

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
logging.StreamHandler(sys.stdout)


async def delay_printer(delay: float, msg: str) -> None:
    logging.debug(f"StartTime:{time.time()}")
    await asyncio.sleep(delay)
    logging.debug(msg=f"Success!Message:{msg}")


async def main():
    await delay_printer(1, "hello1")
    await delay_printer(1, "hello2")


if __name__ == "__main__":
    print("ok")
    asyncio.run(main())
    print("ok")
