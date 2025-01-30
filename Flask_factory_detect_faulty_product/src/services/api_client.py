import aiohttp
import asyncio

async def solve_model(url, access_key, image):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url,
            auth=aiohttp.BasicAuth("kdt2025_1-22", access_key),
            headers={"Content-Type": "image/jpeg"},
            data=image
        ) as response:
            print(f"Request finished with status: {response.status}")
            return await response.json()

async def call_two_models(urls, access_key, image):
    result1, result2 = await asyncio.gather(
        solve_model(urls[0], access_key, image),
        solve_model(urls[1], access_key, image)
    )
    return result1, result2
