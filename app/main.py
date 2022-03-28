from fastapi import FastAPI
from mangum import Mangum
# from app.core import config

app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"This is our secret key value: Secret Value" }

handler = Mangum(app)
