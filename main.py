from fastapi import FastAPI

app = FastAPI()

@app.get("/firstStep")
async def root():
    return {"message": "I started FastAPI! Bro new era...."}