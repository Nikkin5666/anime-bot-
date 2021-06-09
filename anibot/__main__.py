import asyncio
from pyrogram import Client, idle
from . import anibot


async def main():
    await asyncio.gather(anibot.start())
    await idle()
    await asyncio.gather(anibot.stop())

asyncio.get_event_loop().run_until_complete(main())