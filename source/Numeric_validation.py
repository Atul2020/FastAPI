import uvicorn
from fastapi import FastAPI,Path

app = FastAPI()


@app.get("/items/{item_id}")
async def get_items(item_id: str = Path(..., min_length = 2, max_length = 10, regex="^Item\d{1,6}")):
   return {"item_id": item_id}


if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)