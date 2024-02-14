from fastapi import FastAPI
from routers import invoices

app = FastAPI()

app.include_router(invoices.router)


@app.get("/", summary="home")
async def root():
    return {"message": "Hello World"}
