# Setup with Docker

[Русский](../ru/docker.md) | **English**

### Dependencies

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

The first thing you need to do is set up your environment variables.
You can read how to configure the environment variable file in the section [Environment Variables](#enviroment)

Next, run the project using Docker:

    cd docker
    docker-compose up --build -d
    
After that open your browser and go to **http:localhost:8000**