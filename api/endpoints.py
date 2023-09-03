from datetime import datetime

import pytz
from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse

from utils.mongo import mongo_obj
from api import api_response

sensor_router = APIRouter(prefix="/sensor", tags=["sensor"])


@sensor_router.get("/readings/by-time")
def get_sensor_readings_by_timestamp(
        start_timestamp: datetime = Query(..., title="Start timestamp", description="Start timestamp"),
        end_timestamp: datetime = Query(..., title="Start timestamp", description="Start timestamp"),
        timezone: str = Query(..., title="Timezone", description="Timezone")
) -> JSONResponse:
    """
    API route to get sensor readings by given timestamp.
    :param start_timestamp: Start timestamp
    :param end_timestamp: End timestamp
    :param timezone: Time zone
    :return: Return sensors readings fetched by timestamp
    """
    response: dict = api_response.copy()

    try:
        readings: list[dict] = mongo_obj.get_sensor_readings_by_time(
            start_timestamp.replace(tzinfo=pytz.timezone(timezone)).isoformat(),
            end_timestamp.replace(tzinfo=pytz.timezone(timezone)).isoformat()
        )
        if readings:
            response["status"] = "success"
            response["code"] = status.HTTP_200_OK
            response["message"] = "Sensor readings fetched successfully"
            response["data"] = readings
        else:
            response["status"] = "failure"
            response["code"] = status.HTTP_404_NOT_FOUND
            response["message"] = "No sensor readings found for given time"
    except Exception as e:
        response["status"] = "failure"
        response["code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["message"] = f"Internal server error: {e}"

    return JSONResponse(status_code=response.get("code"), content=response)


@sensor_router.get("/readings/last-ten")
def get_sensor_readings_by_timestamp(
        name: str = Query(..., title="Sensor", description="Name of a sensor")
) -> JSONResponse:
    """
    API route to get sensor readings by given timestamp.
    :param name: Start timestamp
    :return: Return sensors readings fetched by timestamp
    """
    response: dict = api_response.copy()

    try:
        readings: list[dict] = mongo_obj.get_last_ten_readings_by_sensor(name)
        if readings:
            response["status"] = "success"
            response["code"] = status.HTTP_200_OK
            response["message"] = f"Last 10 readings of a {name} sensor fetched successfully"
            response["data"] = readings
        else:
            response["status"] = "failure"
            response["code"] = status.HTTP_404_NOT_FOUND
            response["message"] = "No sensor readings found for given sensor"
    except Exception as e:
        response["status"] = "failure"
        response["code"] = status.HTTP_500_INTERNAL_SERVER_ERROR
        response["message"] = f"Internal server error: {e}"

    return JSONResponse(status_code=status.HTTP_200_OK, content=response)
