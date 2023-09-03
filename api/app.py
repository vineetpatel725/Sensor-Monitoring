from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints import sensor_router

app = FastAPI(title="Sensor Monitoring")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensor_router)
