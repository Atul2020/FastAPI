import uvicorn
from fastapi import FastAPI,Query
from typing import List

app = FastAPI()
#String_validations for query parameters
@app.get("/items/")
async def get_items(item_id: str = Query(None,min_length = 2, max_length = 10,regex="^Item\d{1,6}")): #we are defining the max and min length
    return {"item": item_id}

@app.get("/items/")
async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], min_length = 2, max_length = 10)):
    results = {"items": item_id}
    return results

@app.get("/items/")
async def get_items(item_id: List[str] = Query(["Pen", "Pencil"], title = "Item List",
                                            description = "List of items to be returned.",  #adding metadata and depricating parameters
                                   min_length = 2, max_length = 10, deprecated = True)):
     results = {"items": item_id}
     return results

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)