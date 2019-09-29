import asyncio

async def task(task_name):
    print(f"{task_name} started")
    await asyncio.sleep(1)
    print(f"{task_name} finished")

async def main():
    await asyncio.gather(
        *[task(f"Task {i}") for i in range(5)]   
    )

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())