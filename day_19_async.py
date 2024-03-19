import asyncio


async def hello_word():
    print("Started 🌍")
    await asyncio.sleep(3)  # asleep | async function
    print("Hello, World!! 🌍")


# asyncio.run(hello_word())


# Task 1 countdown

# 3
# 2
# 1
# Happy New year


# async def count_down():
#     print(3)
#     await asyncio.sleep(1)
#     print(2)
#     await asyncio.sleep(1)
#     print(1)
#     await asyncio.sleep(1)
#     print("Happy New Year")


# asyncio.run(count_down())


# Task - 2
# create a reuasble function


# async def print_num(num):
#     print(num)
#     await asyncio.sleep(1)


# async def count_down():
#     await print_num(3)
#     await print_num(2)
#     await print_num(1)
#     print("Happy New Year")


# asyncio.run(count_down())


# async def print_num(num):
#     await asyncio.sleep(1)
#     print(num)


# async def count_down():
#     for num in range(3, 0, -1):
#         await print_num(num)
#     await print_num("Happy New Year")


# asyncio.run(count_down())


# Event loop : behind the async function
# code runs in a call stack
# Event loop pushes to stack when the call stack is empty
#

# Async without even loop
# async def background_task():
#     print("Start background task")
#     await asyncio.sleep(3)


# async def main():
#     await background_task()
#     # waiting for background task
#     print("main function says - Hi")


# asyncio.run(main())


# Async with event loop
# async def cooking_eggs():
#     print("eggs cooking")
#     await asyncio.sleep(3)
#     print("Eggs cooked")


# async def make_coffee():
#     print("coffee brewing")
#     await asyncio.sleep(2)
#     print("coffee done")


# Old method
# async def main():
#     # Request to event loop to schedule
#     task1 = asyncio.create_task(cooking_eggs())  # con-currently
#     task2 = asyncio.create_task(make_coffee())
#     # Waiting for the background task
#     print("Bread toast 1")
#     print("Bread toast 2")
#     print("Bread toast 3")

#     await asyncio.wait({task1, task2})


# asyncio.run(main())


# async def main():
#     # Request to event loop to schedule
#     task1 = asyncio.create_task(cooking_eggs())  # con-currently
#     task2 = asyncio.create_task(make_coffee())
#     # Waiting for the background task
#     print("Bread toast 1")
#     print("Bread toast 2")
#     print("Bread toast 3")

#     await asyncio.gather(task1, task2)


# asyncio.run(main())


# async def cooking_eggs():
#     print("eggs cooking")
#     await asyncio.sleep(3)
#     print("Eggs cooked")
#     return f"Data - Eggs"


# async def make_coffee():
#     print("coffee brewing")
#     await asyncio.sleep(2)
#     print("coffee done")
#     return f"Data - coffee"


# async def make_cereal():
#     print("Making cereal bowl")
#     await asyncio.sleep(4)
#     print("Cereal done")
#     return f"Data - cereal"


# async def main():
#     # Request to event loop to schedule

#     all_tasks = [
#         asyncio.create_task(cooking_eggs()),
#         asyncio.create_task(make_coffee()),
#         asyncio.create_task(make_cereal()),
#     ]
#     # Waiting for the background task
#     print("Bread toast 1")
#     print("Bread toast 2")
#     print("Bread toast 3")

#     # await asyncio.gather(all_tasks[0], all_tasks[1],all_tasks[2])
#     # Order given in create task will be order of data
#     data = await asyncio.gather(*all_tasks)
#     print(data)


# asyncio.run(main())


async def cooking_eggs():
    print("eggs cooking")
    await asyncio.sleep(3)
    print("Eggs cooked")
    return f"Data - Eggs"


async def make_coffee():
    print("coffee brewing")
    await asyncio.sleep(2)
    print("coffee done")
    return f"Data - coffee"


async def make_cereal():
    print("Making cereal bowl")
    await asyncio.sleep(4)
    print("Cereal done")
    return f"Data - cereal"


async def main():
    # Request to event loop to schedule

    all_tasks = [
        cooking_eggs(),
        make_coffee(),
        make_cereal(),
    ]

    # Waiting for the background task
    print("Bread toast 1")
    print("Bread toast 2")
    print("Bread toast 3")

    # await asyncio.gather(all_tasks[0], all_tasks[1],all_tasks[2])
    # Order given in create task will be order of data
    data = await asyncio.gather(*all_tasks)
    print(data)


asyncio.run(main())
