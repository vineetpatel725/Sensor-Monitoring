import json
import time
from uuid import uuid4
from random import uniform
from datetime import datetime, timezone

from mqtt import payload, sensors
from utils.mosquitto import MQTT

mqtt_obj: MQTT = MQTT()


def publish_reading(sensor: str) -> None:
    """
    Function which is responsible to send sensor reading to a particular topic like "sensors/temperature".
    :param sensor: Name of sensor likes temperature, humidity etc.
    :return: None
    """
    try:
        sensor_payload: dict = payload.copy()

        # updating JSON payload of a temperature sensor
        sensor_payload["sensor_id"] = uuid4().hex
        sensor_payload["sensor"] = sensor
        sensor_payload["value"] = round(uniform(-40, 250), 2)
        sensor_payload["timestamp"] = datetime.now().astimezone(tz=timezone.utc).isoformat()

        mqtt_obj.publish(topic=f"sensors/{sensor}", data=json.dumps(sensor_payload))

    except Exception as e:
        print(f"Error occurred: {e.with_traceback()}")


def main() -> None:
    """
    Main function which send multiple sensors reading to a function which will publish that readings into a
    particular topic like sensor/humidity.
    :return: None
    """
    while True:
        _ = list(
            map(
                publish_reading, sensors
            )
        )
        time.sleep(60)
