import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"Message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
