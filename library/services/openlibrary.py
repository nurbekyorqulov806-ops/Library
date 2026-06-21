import aiohttp

async def search_books(query):
    url = f"https://openlibrary.org/search.json?q={query}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            return await r.json()
        

