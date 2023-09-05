## Servcice Overview

### 1 Redis
>Container Name: redis
Image: redis:latest
>Ports: Maps port 6379 on the host to port 6379 in the container, allowing external access to the Redis server.
Description: Redis is an in-memory data store used as a cache and message broker in various applications. It provides fast data retrieval and storage capabilities.
### 2 MongoDB
>Container Name: mongo
Image: mongo:latest
>Ports: Maps port 27017 on the host to port 27017 in the container, enabling external access to the MongoDB server.
Environment Variables: Sets up the root username and password for MongoDB.
>Description: MongoDB is a NoSQL database used for storing and managing structured and unstructured data. It's known for its flexibility and scalability.
### 3 Eclipse Mosquitto (MQTT Broker)
>Container Name: mosquitto
Image: eclipse-mosquitto:latest
>Ports: Maps port 1888 on the host to port 1888 in the container for MQTT communication.
Volumes: Mounts configuration, password, data, and log directories from the host to the container.
>Description: Mosquitto is an MQTT broker that facilitates lightweight and efficient messaging between IoT devices. It is commonly used for real-time data exchange in IoT applications.
### 4 Sensor Monitoring App
>Container Name: sensor-monitoring-app
Image: sensor-monitoring-app
>Build Context: Specifies the context for building the Docker image, likely in the current directory.
Ports: Maps port 8000 on the host to port 8000 in the container (adjust if needed).
>DNS Configuration: Sets the DNS server to 8.8.8.8.
Dependencies: Specifies that this service depends on Redis, MongoDB, and Eclipse Mosquitto.
>Description: This service appears to be the core application that monitors sensors. It may interact with the other services (Redis, MongoDB, and Mosquitto) for data storage and communication.
### Internal Network
>Driver: Uses the bridge network driver for internal communication between containers.
IP Addressing: Configures an internal IP address subnet (192.168.8.0/16) for the containers, each with its unique IP address.
