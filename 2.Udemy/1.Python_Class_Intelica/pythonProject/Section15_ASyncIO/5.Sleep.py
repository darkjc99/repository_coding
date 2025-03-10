import asyncio


async def counter(e):
    print("Starting task")
    for i in range(e):
        print(i)
        if i % 10_000 == 0:
            await asyncio.sleep(0)


async def main():
    print("Started")
    # result = await asyncio.sleep(1, result={"item": 123})
    # result = await asyncio.sleep(0)
    # print(result)

    task = asyncio.create_task(counter(100_000_000))
    task.cancelled()
    await asyncio.sleep(1)
    task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
