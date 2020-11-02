import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/language/")
async def langauge(name: str = Form(...), type: str = Form(...)):
    return {"name": name, "type": type}

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)