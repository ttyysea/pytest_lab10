from mangum.platforms.aws.adapter import AWSLambdaAdapter
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "world"}


handler = AWSLambdaAdapter(app)