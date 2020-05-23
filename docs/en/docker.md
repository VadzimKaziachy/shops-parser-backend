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

Also, for the application to work, you will need [shops-parser](https://github.com/VadzimKaziachy/shops-parser).
You can read about how to install [shops-parser](https://github.com/VadzimKaziachy/shops-parser) [here](https://github.com/VadzimKaziachy/shops-parser/blob/master/README.md).