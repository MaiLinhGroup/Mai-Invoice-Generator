from fastapi import FastAPI

app = FastAPI()
favicon = "static/favicon.ico"


@app.get("/")
async def root():
    return {"message": "Hello World"}
