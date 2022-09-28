from asyncio import Lock
import os
import math
import signal
from time import time, sleep
from threading import Thread

from cryptofeed import FeedHandler
from cryptofeed.defines import TRADES
from cryptofeed.exchanges import Bitstamp

lock = Lock()
all_elapsed = []


def percentile(data, perc: int):
    size = len(data)
    return data[int(math.ceil((size * perc) / 100)) - 1]


async def trade(**kwargs):
    receipt_timestamp = kwargs["receipt_timestamp"]
    elapsed = int((time() - receipt_timestamp) * 1000000)
    print(f"{kwargs}, elapsed={elapsed}us")
    await lock.acquire()
    all_elapsed.append(elapsed)
    lock.release()


def timeout(max_len):
    while True:
        sleep(1)
        if len(all_elapsed) >= max_len:
            os.kill(os.getpid(), signal.SIGINT)


def main():
    fh = FeedHandler()
    fh.add_feed(
        Bitstamp(
            pairs=["BTC-USD", "ETH-USD", "BTC-GBP", "ETH-GBP"],
            channels=[TRADES],
            callbacks={TRADES: trade}
        )
    )
    fh.run()


if __name__ == "__main__":
    thread = Thread(target=timeout, kwargs={"max_len": 200})
    thread.start()

    try:
        print("Starting feedhandler...")
        main()
    finally:
        all_elapsed = sorted(all_elapsed)
        print("    Runtime summary    ")
        print("=======================")
        print(f"Number: {len(all_elapsed)}")
        print(f"Median: {percentile(all_elapsed, 50)}")
        print(f"90-pct: {percentile(all_elapsed, 90)}")
        print(f"95-pct: {percentile(all_elapsed, 95)}")
        print(f"99-pct: {percentile(all_elapsed, 99)}")
