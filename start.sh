#!/bin/bash

# Command to start MQTT Publisher
nohup python3 main.py -p >> publisher.out &

# Command to start MQTT Subscriber
nohup python3 main.py -s >> subscriber.out &

# Command to start REST API
nohup python3 main.py -r >> rest_api.out &

# Keep the script running to prevent the container from exiting
tail -f /app/rest_api.out