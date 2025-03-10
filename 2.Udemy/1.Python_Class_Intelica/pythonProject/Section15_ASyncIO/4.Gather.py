import asyncio


async def fetch_data(data: int) -> dict:
    print("Fetching data...")
    await asyncio.sleep(1)
    if data == 0:
        raise Exception("No data")
    return {"data": data}


async def main():
    tasks = asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3),
        fetch_data(0),
        return_exceptions=True,
    )
    results = await tasks

    print(results)


asyncio.run(main())
