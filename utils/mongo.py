from datetime import datetime

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from config import global_config


class Mongo(object):
    """
    MongoDB class for storing or retrieving records from collections
    """
    print(f"Connecting MongoDB database")
    try:
        mongo_client: MongoClient = MongoClient(
            host=global_config.get("mongodb", "host"),
            port=global_config.getint("mongodb", "port"),
            username=global_config.get("mongodb", "username"),
            password=global_config.get("mongodb", "password")
        )
        print(f"Connected to MongoDB database")
    except ConnectionFailure as e:
        print(f"Connection failure: {e}")

    def __init__(self, db_name: str):
        self.db = self.mongo_client[db_name]
        print(f"Current database: {self.db}")

    def get_all_collections(self) -> list:
        """
        Function to get all collection of a current database.
        :return: List of collections
        """
        return self.db.list_collection_names()

    def store_readings(self, reading: dict) -> str:
        """
        Function to store received readings into "readings" collection.
        :param reading: Dictionary that contains reading of a sensor
        :return: Return inserted id of a record
        """
        print(f"Storing sensor reading {reading} into 'reading' collection")
        reading = self.db.readings.insert_one(reading)
        print(f"Reading stored and inserted id is {reading.inserted_id}")
        return reading.inserted_id

    def get_sensor_readings_by_time(
            self,
            start_timestamp: str | datetime,
            end_timestamp: str | datetime = None
    ) -> list[dict]:
        """
        Function to fetch sensors readings by given time.
        :param start_timestamp: Start timestamp
        :param end_timestamp: End timestamp
        :return: Return list which contains sensors readings
        """
        readings = self.db.readings.find(
            {
                "timestamp": {
                    "$gte": start_timestamp,
                    "$lte": end_timestamp
                },
            },
            {"_id": False}
        )
        return list(readings)

    def get_last_ten_readings_by_sensor(self, sensor: str) -> list[dict]:
        """
        Function to fetch last ten readings of a particular sensor.
        :param sensor: Sensor
        :return: Return list which contains last ten readings of a particular sensor
        """
        readings = self.db.readings.find(
            {"sensor": sensor}, {"_id": False}
        ).sort(
            [("timestamp", -1)]
        ).limit(10)
        return list(readings)


mongo_obj: Mongo = Mongo("sensors")
