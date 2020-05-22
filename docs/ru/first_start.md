# Первый старт

**Русский** | [English](../en/first_start.md)

Вы можете запустить проект **shops-parser-backend** локально использовую **Pipenv**.

### Зависимости

* [pip3](https://github.com/pypa/pip)
* [Pipenv](https://pypi.org/project/pipenv/)
* [Python 3.7](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)

### Установка

Прежде всего, установите [Pipenv](https://pypi.org/project/pipenv/), выполните команды:

    pip install pipenv

Перейдите в папку [backend](../../docker/backend) и активируйте среду:

    pipenv shell

Убедитесь, что окружение было создано и активировано.

Далее необходимо установить все необходимые пакеты для приложения.

    pipenv install
    
Следующим шагом является настройка переменных среды.
Вы можете прочитать, как настроить файл переменных среды, в разделе [Переменные среды](enviroment.md)

После того, как все было настроено, вы можете запустить проект. Первое, что вам нужно сделать, это выполнить миграции
по настройке базы данных:

    pipenv run python manage.py migrate

После того, как все вышеперечисленное было сделано, вы можете запустить проект. Для этого выполните команду ниже,
это позволит вам запустить проект:

    pipenv run python manage.py runserver

Теперь откройте проект в [браузере](http://localhost:8000).