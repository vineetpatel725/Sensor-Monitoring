import argparse

import uvicorn

from config import global_config
from api.app import app
from mqtt import publisher, subscriber

parser = argparse.ArgumentParser(
    description="Options and arguments for sensor monitoring services",
    allow_abbrev=False
)
parser.add_argument(
    "-p", "--mqtt-publisher", action="store_true", help="to start mqtt publisher"
)
parser.add_argument(
    "-s", "--mqtt-subscriber", action="store_true", help="to start mqtt subscriber"
)
parser.add_argument(
    "-r", "--rest-api", action="store_true", help="to start REST API"
)
args = parser.parse_args()

if args.mqtt_publisher:
    publisher.main()
elif args.mqtt_subscriber:
    subscriber.main()
elif args.rest_api:
    uvicorn.run(app=app, host=global_config.get("uvicorn", "host"), port=global_config.getint("uvicorn", "port"))
else:
    parser.print_help()
