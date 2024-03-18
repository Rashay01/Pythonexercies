import requests
from pprint import pprint
import aiohttp
import asyncio
from time import time

TOKEN = "0024363e8dac42d29e693412241503"

# def get_place_temp(city_name):
#     full_url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
#     response = requests.get(full_url, verify=False)
#     country_weather = response.json()
#     return country_weather['location']['name'], country_weather['current']['temp_c']


# Async - aiohttp
async def get_city_temp(city_name):
    print(f"Getting temp of {city_name}")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            print(
                f"The temperature in {weather['location']['name']} is {weather['current']['temp_c']}°C"
            )


# async def main():
#     # asyncio.run(get_city_temp("Cape Town"))
#     # asyncio.run(get_city_temp("Chennai"))
#     # asyncio.run(get_city_temp("Johannesburg"))
#     # asyncio.run(get_city_temp("Durban"))
#     all_tasks = [
#         asyncio.create_task(get_city_temp("Cape Town")),
#         asyncio.create_task(get_city_temp("Chennai")),
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Durban")),
#     ]
#     await asyncio.gather(*all_tasks)


# Task 1
# async def main():
#     all_tasks = [
#         get_city_temp("Cape Town"),
#         get_city_temp("Chennai"),
#         get_city_temp("Johannesburg"),
#         get_city_temp("Durban"),
#     ]
#     await asyncio.gather(*all_tasks)


# Task2
# async def main():
#     all_tasks = [
#         asyncio.create_task(get_city_temp("Cape Town")),
#         asyncio.create_task(get_city_temp("Chennai")),
#         asyncio.create_task(get_city_temp("Johannesburg")),
#         asyncio.create_task(get_city_temp("Durban")),
#     ]
#     await asyncio.gather(*all_tasks)


# Task 3
# cities = []
# Clue: gather
# 2s + 0.2s (API time)


# async def main():
#     cities = [
#         "New York",
#         "Tokyo",
#         "London",
#         "Paris",
#         "Dubai",
#         "Singapore",
#         "Sydney",
#         "Istanbul",
#         "Hong Kong",
#         "Cape Town",
#     ]
#     all_tasks = [asyncio.create_task(get_city_temp(city)) for city in cities]

#     await asyncio.gather(*all_tasks)


# start_time = time()
# asyncio.run(main())
# end_time = time()
# print(f"Time taken {end_time-start_time}")


# Task 4

cities = [
    "New York",
    "Tokyo",
    "London",
    "Paris",
    "Dubai",
    "Singapore",
    "Sydney",
    "Istanbul",
    "Hong Kong",
    "Cape Town",
]


async def get_city_temp(city_name):
    print(f"Getting temp of {city_name}")
    url = f"http://api.weatherapi.com/v1/current.json?key={TOKEN}&q={city_name}&aqi=no"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            weather = await response.json()
            return weather["location"]["name"], weather["current"]["temp_c"]


async def main():
    all_tasks = [asyncio.create_task(get_city_temp(city)) for city in cities]
    all_cities_temp = dict(await asyncio.gather(*all_tasks))
    pprint(all_cities_temp)


start_time = time()
asyncio.run(main())
end_time = time()
print(f"Time taken {end_time-start_time}")
