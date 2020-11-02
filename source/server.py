import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"Message": "Hello World"}

@app.get("/items/{item_id}") #path parameter
async def read_item(item_id):
    return {"item_id": item_id}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): # query parameters
    return fake_items_db[skip : skip + limit]

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
