import os

from fastapi import FastAPI

from app.checkout.router import router as checkout_router

app = FastAPI(title="Checkout Commerce", version="0.1.0")

app.include_router(checkout_router)


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", 8005))
    uvicorn.run(app, host=host, port=port)
