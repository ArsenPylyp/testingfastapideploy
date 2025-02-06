from fastapi import FastAPI, Depends

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    print("base cleaned")
    await create_tables()
    print("started base")
    yield
    print("closing")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
