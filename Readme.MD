
# Sensor Monitoring

System is designed to simulate the behavior of various sensors, ensuring accurate and reliable data generation. We continuously monitor the readings from these sensors, offering real-time insights into the environment or system being monitored. Additionally, we provide a user-friendly API that allows you to easily retrieve specific data based on your criteria. Whether you need last ten readings of a temperature sensor or readings within a certain timeframe, our API makes it effortless to access the information you need.
## Installation

<font size="6">**1 Set Up MongoDB Credentials**</font>
Set your desired MongoDB username and password in the environment variables as shown below:.
```yaml
environment:
  MONGO_INITDB_ROOT_USERNAME: system
  MONGO_INITDB_ROOT_PASSWORD: zsWGd4L4JyeKXaI
```
Additionally, set the static IPv4 address in the ipv4_address field within the networks section:
```yml
networks:
  internal_network:
    ipv4_address: 192.168.8.3
```  
Update your Python app's configuration file to include the MongoDB host, username, and password:
```ini
[mongodb]
host = 192.168.8.3
username = system
username = zsWGd4L4JyeKXaI
```

<font size="4">**2 Configure Mosquitto (MQTT)**</font>
>Set the absolute paths to your Mosquitto configuration and password files in the volumes section:
```yaml
volumes:
  - "/home/alex/Documents/mosquito.config:/mosquitto/config/mosquitto.conf"
  - "/home/alex/Documents/mosquito.pwd:/mosquitto/config/mosquitto.pwd"
  - "/mosquitto/data"
  - "/mosquitto/log"
```
Additionally, set the static IPv4 address in the ipv4_address field within the networks section:
```yaml
networks:
  internal_network:
    ipv4_address: 192.168.8.4
```
Update your Python app's configuration file to include the Mosquitto (MQTT) host, username, and password:
```ini
[mosquitto]
host = 192.168.8.4
username = system
password = PsAnd9L8JyeQXaU
```

### 3 Configure redis 
Set the static IPv4 address in the ipv4_address field within the networks section:
```yaml
networks:
  internal_network:
    ipv4_address: 192.168.8.2
```
Update your Python app's configuration file to include the Redis host:
```ini
[redis]
host = 192.168.8.2
```

### 4 Network Configuration
Update the subnet configuration in the docker-compose.yml file under the newly created network. Adjust the subnet and gateway values as needed:
```yaml
networks:
  internal_network:
    driver: bridge
    ipam:
      config:
        - subnet: 192.168.8.0/16
          gateway: 192.168.8.1
```
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
