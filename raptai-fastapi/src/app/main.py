from src.dependencies.database import connect, disconnect, create_tables
from src.core.config import settings
from src.api.v1.routers import router as api_router
from fastapi import FastAPI
from contextlib import asynccontextmanager
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect()
    await create_tables()
    yield
    await disconnect()

app = FastAPI(title=settings.PROJECT_NAME, lifespan=lifespan)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)
