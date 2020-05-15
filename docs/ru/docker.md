# Настройка с помощью Docker

**Русский** | [English](../en/docker.md)

### Зависимости

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Установка

Первое, что вам нужно сделать, это настроить переменные окружения.
Вы можете прочитать, как настроить файл переменной среды в разделе [Переменные окружения](#enviroment)

Далее запустите проект с помощью **Docker**:

    cd docker
    docker-compose up --build -d
    
После этого откройте ваш браузер и перейдите на **http:localhost:8000**