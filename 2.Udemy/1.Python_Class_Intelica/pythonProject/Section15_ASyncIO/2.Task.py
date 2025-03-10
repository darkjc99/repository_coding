import asyncio


async def fetch_data(data: int) -> dict:
    print("Fetching data...")
    await asyncio.sleep(6)
    return {"data": data}


async def main():
    task = asyncio.create_task(fetch_data(100))

    try:
        data: dict = await asyncio.wait_for(task, timeout=5)
        print(data)
        # if task.done():
        #     data: dict = task.result()
        #     print(data)
        # else:
        #     print("Data not ready")
    except asyncio.CancelledError:
        print("Task was cancelled")


asyncio.run(main())
