import sys
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routers.solution import router as backend

app = FastAPI(title="fonoma-backend-test")

headers = {
    "Content-Type",
    "X-Amz-Date",
    "Authorization",
    "X-Api-Key",
    "X-Amz-Security-Token",
    "X-Amz-User-Agent",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Credentials",
    "Access-Control-Allow-Origin"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = headers,
)

app.include_router(backend.router)

@app.middleware("http")
async def request_logger(request: Request, call_next):
    response = await call_next(request)
    return response