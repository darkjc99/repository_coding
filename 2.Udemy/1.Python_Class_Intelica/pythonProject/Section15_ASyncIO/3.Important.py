import asyncio


async def count():
    for i in range(10**10):
        print(i)

        if i % 10_000 == 0:
            await asyncio.sleep(0.01)


async def main():
    task = asyncio.create_task(count())

    await asyncio.sleep(2)
    task.cancel()
    print("Task cancelled")
    await task


if __name__ == "__main__":
    asyncio.run(main())
