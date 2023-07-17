from fastapi import FastAPI as fp
from typing import Optional
from pydantic import BaseModel

from shortener import shortener

class ItemFull(BaseModel):
    url: str
    shortend: Optional[str] = None

class Item(BaseModel):
    shortend: Optional[str] = None
    

app = fp()

@app.get("/shortFull/{url}")
async def shortenFull(url: str):
    short = shortener(url)
    itemFull = {"url": url, "shortend": short}
    return itemFull

@app.get("/short/{url}")
async def shorten(url: str):
    short = shortener(url)
    item = {"shortend": short}
    return item