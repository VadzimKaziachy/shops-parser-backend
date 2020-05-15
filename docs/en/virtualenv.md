# Setup with Virtualenv

[Русский](../ru/virtualenv.md) | **English**

You can run the django-parser-demo project locally without installing Docker, and just use Virtualenv,
which is the recommended installation approach for Django itself.

### Dependencies

* [pip3](https://github.com/pypa/pip)
* [Python 3.7](https://www.ics.uci.edu/~pattis/common/handouts/pythoneclipsejava/python.html)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)

### Installation

First of all, activate the environment. To do this, go to the project root and execute the commands:

    virtualenv --python=python3 venv              
    source venv/bin/activate

Make sure that virtualenv is activated,
otherwise further actions will entail the installation of the globano project in your system.

Next, you need to install all the necessary packages for the application.
To do this, go to the [docker/web](../../docker/web) folder and install the packages:

    cd docker/web
    pip install -r requirements.txt
    
The next step is to configure our local environment variables. 
You can read how to configure the environment variable file in the section [Environment variables](enviroment.md)

After everything has been configured, you can start the project. The first thing you need to do is perform migrations
to set up a database:

    python manage.py migrate

After all the above has been done, you can run project. To do this, run the command below,
it will allow you to run the project:

    python manage.py runserver

Now open the project in the [browser](http://localhost:8000).