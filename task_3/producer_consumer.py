import random
import asyncio
from asyncio import Lock, Condition

warehouse = []

max_elements = 10

warehouse_lock = Lock()

def is_overflow():
    return len(warehouse) >= max_elements

def is_underflow():
    return len(warehouse) == 0


async def producer(id, overflow_condition, underflow_condition):
    while True:
        x = random.randint(a=1, b=10000)

        await warehouse_lock.acquire()
        if not is_overflow():
            warehouse.append(x)
            print('Producer {} produced number {}'.format(id, x))
            warehouse_lock.release()
        else:
            async with overflow_condition:
                warehouse_lock.release()
                print("Overflow. Producer {} waiting".format(id))
                await overflow_condition.wait()

        async with underflow_condition:
            underflow_condition.notify()
        await asyncio.sleep(random.random() * 5.0)


async def consumer(id, overflow_condition, underflow_condition):
    while True:
        await warehouse_lock.acquire()
        if not is_underflow():
            x = warehouse.pop(0)
            print('Consumer {} consumed number {}'.format(id, x))
            warehouse_lock.release()
        else:
            async with underflow_condition:
                warehouse_lock.release()
                print("Underflow. Consumer {} waiting".format(id))
                await underflow_condition.wait()

        async with overflow_condition:
            overflow_condition.notify()
        await asyncio.sleep(random.random() * 2.0)

async def main():

    overflow_condition = Condition()

    underflow_condition = Condition()

    tasks = []

    for i in range(10):
        tasks.append(asyncio.create_task(producer(i, overflow_condition, underflow_condition)))

    for i in range(2):
        tasks.append(asyncio.create_task(consumer(i, overflow_condition, underflow_condition)))

    await tasks[0]


if __name__=="__main__":
    asyncio.run(main())