from fastapi import FastAPI

app = FastAPI(title="My File Handle API")

@app.get("/")
async def index():
    return {"message": "It works"}