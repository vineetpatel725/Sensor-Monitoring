import json
from typing import Any

from mqtt import sensors
from utils.imdb import imdb_obj
from utils.mongo import mongo_obj
from utils.mosquitto import mqtt_obj


def on_message_receive(client: Any, userdata: Any, msg: Any) -> None:
    """
    Function which will receive all messages from subscribed topics
    :param client: Any
    :param userdata: Any
    :param msg: Any
    :return: None
    """
    topic: str = msg.topic
    payload: dict = json.loads(msg.payload.decode('utf-8'))

    print(f"Topic: {topic} :: Payload: {payload}")
    inserted_id: str = mongo_obj.store_readings(payload)
    print(f"Reading is saved and inserted id is {inserted_id}")

    imdb_obj.push_element("latest_readings", msg.payload.decode('utf-8'))
    imdb_obj.pop_elements_by_range("latest_readings", 0, 9)


def main() -> None:
    """
    Main function which receive multiple sensors reading from topics likes "sensor/humidity" for further use.
    :return: None
    """
    topics: list = list(
        map(
            lambda s: f"sensors/{s}", sensors
        )
    )
    mqtt_obj.subscribe(topic=topics, on_message=on_message_receive)
