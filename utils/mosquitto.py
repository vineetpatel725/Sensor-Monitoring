from typing import Callable

from paho.mqtt import client as mqtt

from config import global_config


class MQTT(object):
    """
    Mosquitto MQTT class for publishing messages and receiving messages from topics
    """
    print(f"Connecting Mosquitto MQTT client")
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(
        username=global_config.get("mosquitto", "username"),
        password=global_config.get("mosquitto", "password")
    )
    mqtt_client.connect(
        host=global_config.get("mosquitto", "host"),
        port=global_config.getint("mosquitto", "port"),
        keepalive=global_config.getint("mosquitto", "keepalive")
    )
    print(f"Connected to Mosquitto MQTT client")

    @classmethod
    def publish(cls, topic: str, data: str) -> None:
        """
        Class method to publish message into a particular topic.
        :param topic: Name of a topic
        :param data: Data to be published
        :return: None
        """
        cls.mqtt_client.publish(
            topic=topic,
            payload=data
        )
        print(f"Data published {data} to topic {topic}")

    @classmethod
    def subscribe(cls, topic: list, on_message: Callable) -> None:
        """
        Class method to subscribe/consume messages which are published to the given topic.
        :param topic: List of a topic
        :param on_message: Name of a function which calls when message receive
        :return: None
        """
        print(f"Topics {topic} Subscribed")
        _ = list(
            map(
                cls.mqtt_client.subscribe, topic
            )
        )
        cls.mqtt_client.on_message = on_message
        cls.mqtt_client.loop_forever()


mqtt_obj: MQTT = MQTT()
