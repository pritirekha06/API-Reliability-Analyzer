import asyncio
import time
import httpx

async def hit_api(client, url, results):
    start = time.time()
    try:
        response = await client.get(url, timeout=5)
        elapsed = time.time() - start
        results.append({
            "success": response.status_code < 400,
            "time": elapsed
        })
    except Exception:
        results.append({
            "success": False,
            "time": None
        })

async def run_test(url: str, duration: int, rps: int):
    results = []
    
    async with httpx.AsyncClient() as client:
        for _ in range(duration):
            tasks = []
            for _ in range(rps):
                tasks.append(hit_api(client, url, results))
            await asyncio.gather(*tasks)
            await asyncio.sleep(1)
    
    return results