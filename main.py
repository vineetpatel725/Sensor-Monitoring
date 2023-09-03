import argparse

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
args = parser.parse_args()

if args.mqtt_publisher:
    publisher.main()
elif args.mqtt_subscriber:
    subscriber.main()
else:
    parser.print_help()
