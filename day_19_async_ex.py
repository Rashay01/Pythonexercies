from pprint import pprint
import json
import aiohttp
import asyncio
from time import time


# async def get_users_name():
#     url = "https://65f82847b4f842e808871317.mockapi.io/users"
#     # print("User names:")
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             users = await response.json()
#             for user in users:
#                 print(user["name"])


async def get_users_name():
    url = "https://65f82847b4f842e808871317.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            return users


# async def main():
#     users = await get_users_name()
#     ans = [user["name"] for user in users]
#     print(".\n".join(ans))


# asyncio.run(main())

# Delete user with id = 15


async def delete_users_by_id(id):
    url = f"https://65f82847b4f842e808871317.mockapi.io/users/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            user = await response.json()
            return user


async def get_user_name():
    url = "https://65f82847b4f842e808871317.mockapi.io/users"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            return users


# async def main():
#     users = await get_users_name()
#     users = users[:5]
#     users_tasks = [
#         asyncio.create_task(delete_users_by_id(the_user["id"])) for the_user in users
#     ]
#     users_del = await asyncio.gather(*users_tasks)
#     pprint(users_del)


# asyncio.run(main())


# Task Change all users profile pic to flag
async def change_avatar(id, img_url):
    url = f"https://65f82847b4f842e808871317.mockapi.io/users/{id}"
    body = {"avatar": img_url}
    async with aiohttp.ClientSession() as session:
        async with session.put(url, data=body) as response:
            user = await response.json()
            return user


async def main():
    flag_url = "https://static.vecteezy.com/system/resources/previews/020/297/008/non_2x/south-africa-human-rights-day-march-21-for-greeting-card-poster-banner-template-free-vector.jpg"
    users = await get_users_name()
    users_tasks = [
        asyncio.create_task(change_avatar(the_user["id"], flag_url))
        for the_user in users
    ]
    updated_users = await asyncio.gather(*users_tasks)
    pprint(updated_users)


asyncio.run(main())
