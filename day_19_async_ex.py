from pprint import pprint
import aiohttp
import asyncio
from time import time


async def get_users_name():
    url = "https://65f82847b4f842e808871317.mockapi.io/users"
    # print("User names:")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            users = await response.json()
            for user in users:
                print(user["name"])


async def main():
    await get_users_name()


asyncio.run(main())
