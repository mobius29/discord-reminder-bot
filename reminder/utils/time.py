import asyncio

async def set_timeout(seconds: int, callback, *args, **kwargs):
    await asyncio.sleep(seconds)
    await callback(*args, **kwargs)
