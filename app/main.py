import os

from fastapi import FastAPI

app = FastAPI(title="Checkout Commerce", version="0.1.0")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", 8005))
    uvicorn.run(app, host=host, port=port)
