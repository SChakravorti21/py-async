import asyncio
import random

async def sum_range(start, end, sleep=True):
    """
    Purely for the sake of this example, this function
    will yield (through asyncio.sleep) to allow for 
    interleaving of the summation tasks
    """

    range_sum = 0
    for num in range(start, end):
        print(f"{num}")
        range_sum += num

        if sleep and random.randint(0, 99) < 30:
            # Sleeping for "zero" seconds will yield
            # execution of the current coroutine to run
            # other scheduled coroutines until this one
            # is scheduled again
            await asyncio.sleep(0)

    return range_sum


async def main():
    # Schedule and await simultaneously
    await sum_range(0, 1000)

    # Schedule immediately using `create_task`, await later.
    # The same can be done with `ensure_future`, but that is
    # less readable.
    task = asyncio.create_task(sum_range(0, 1000, sleep=False))
    await asyncio.sleep(2)
    await task
    print("\n\n\n")

    # Schedule all tasks at once using `gather`.
    tasks = [sum_range(10 * i, 10 * i + 10) for i in range(10)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())