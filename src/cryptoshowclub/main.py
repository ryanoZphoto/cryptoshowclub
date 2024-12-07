from fastapi import FastAPI

app = FastAPI(
    title="Crypto Show Club",
    description="A platform for cryptocurrency enthusiasts",
    version="0.1.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Crypto Show Club"}
