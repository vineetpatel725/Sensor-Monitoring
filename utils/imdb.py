from redis import Redis
from redis.exceptions import ConnectionError

from config import global_config


class IMDB(object):
    """
    IMDB class for storing or retrieving data from redis in-memory database.
    """
    print(f"Connecting Redis memory database")
    try:
        redis_client: Redis = Redis(
            host=global_config.get("redis", "host"),
            port=global_config.getint("redis", "port"),
            username=global_config.get("redis", "username"),
            password=global_config.get("redis", "password"),
            decode_responses=True,
            db=global_config.getint("redis", "db")
        )
        redis_client.ping()
        print(f"Connected to Redis memory database")
    except ConnectionError as e:
        print(f"Connection Error: {e}")

    @classmethod
    def push_element(cls, name: str, element: str) -> None:
        """
        Function which push/add element to the head of a list
        :param name: Name of a list
        :param element: Element to be pushed
        :return: None
        """
        print(f"Pushing element {element} into {name} list")
        cls.redis_client.lpush(name, element)
        print(f"Element pushed")

    @classmethod
    def pop_elements_by_range(cls, name: str, start: int, end: int) -> None:
        """
        Function which reduce list to the specific range
        :param name: Name of a list
        :param start: Index starting number
        :param end: Index ending number
        :return: None
        """
        print(f"Reducing list {name} by range {start} to {end}")
        cls.redis_client.ltrim(name, start, end)
        print(f"List reduced")

    @classmethod
    def get_elements(cls, name: str, start: int, end: int) -> None:
        """
        Function which get elements from a given range in the list
        :param name: Name of a list
        :param start: Index starting number
        :param end: Index ending number
        :return: None
        """
        print(f"Fetching elements from a list {name} by range {start} to {end}")
        elements: list = cls.redis_client.lrange(name, start, end)
        print(f"Fetched elements are {elements}")


imdb_obj: IMDB = IMDB()
