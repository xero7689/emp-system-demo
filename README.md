# Initium Media Interview Quest
An interview quest project for Initium Media powered by Django. The goal is to implement a simple yet efficient HR System that allows user login/logout and enables viewing basic employee information.


## Built With
| Package    | Version |
|------------|---------|
| python     | 3.9.10  |
| Django     | 4.2     |
| redis      | 4.5.5   |
| psycopg2   | 2.9.3   |
| uWSGI      | 2.0.20  |


# Installation and Running
## Locally
If you decide to deploy the project locally, install the package by using:

```
pip install -r requirements.txt
```

and do:
```
python manage.py runserver
```

## Dockerizing
To launch the service using `docker-compose`, follow these steps:

1. Before proceeding, make sure you have a `.env` file containing the required environment variables. Refer to the Environment Variables section for more details.

2. Run the following commands to automatically execute the necessary scripts, build a production-ready image, and start the service:
    ```bash
    docker-compose build
    docker-compose up
    ```
3. Check the `http://0.0.0.0:80` for the deploy status.


### .env File
A `.env` file is manually generated or generated using `dotenv`. You should provide the necessary deploying arguments before building the image.

Here is an example template for default .env file:
```
APP_NAME=initium-interview
IMAGE_NAME=initium-interview

GIT_USER=
GIT_PASSWORD=

DEPLOY_STAGE=ut
IS_DEBUG=True

IN_CONTAINER=True

DATABASE_URI=db
DATABASE_DB_NAME=for-development
DATABASE_USER=devel
DATABASE_PASSWD=for-development
CONTAINER_STORAGE_PATH=/var/app_data/static

DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin1234
DJANGO_SUPERUSER_EMAIL=mock_admin@gmail.com
```
