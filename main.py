import asyncio

import aiohttp

from utils.bot import LoungeKitBot


async def main():
    async with aiohttp.ClientSession() as session:
        bot = LoungeKitBot(session)
        await bot.start()

asyncio.run(main())