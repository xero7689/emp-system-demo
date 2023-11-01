# Initium Media Interview Quest

The project implement a Demo HR System powered by Django that provides the following functionality:

- Basic `login`/`logout` functions powered by Django's authentication system
- User registration page to become a system member
- Portal site for viewing basic employee information
- Admin site for managers to configure employee data

## Built With

| Package  | Version |
| -------- | ------- |
| python   | 3.9.10  |
| Django   | 4.2     |
| redis    | 4.5.5   |
| psycopg2 | 2.9.3   |
| uWSGI    | 2.0.20  |

# Installation and Running

## Dockerizing

To launch the service using `docker` with `docker-compose`, follow these steps:

### Configure .env File

A `.env` file is manually generated or generated using `dotenv`.
You should provide the necessary deploying arguments before building the image.

Here is an example template for default .env file:

```
APP_NAME=initium-interview
IMAGE_NAME=initium-interview

GIT_USER=
GIT_PASSWORD=

DEPLOY_STAGE=ut
IS_DEBUG=False

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

You can simply copy these content to `.env` file under the project directory.

### Build Image

Run the following commands to automatically execute the necessary scripts, build a production-ready image:

```bash
docker-compose build
```

### Start the service:

```bash
docker-compose up
```

Check the `http://0.0.0.0` for the deploy status.

## Locally

To deploy the project locally and manually, follow these steps:

### Install the required packages

```
pip install -r requirements.txt
```

### Perform the database migrations

```
python manage.py makemigrations hr_system
python manage.py migrate
```

### Create a superuser admin account

```
python manage.py createsuperuser
```

### Launch the service

```
python manage.py runserver
```

### (Optional) Test the Project

You can run tests to ensure everything is functioning correctly. Run the following command:

```
python manage.py test
```

Finally, check the deployment status by visiting [http://127.0.0.1](http://127.0.0.1)

# How to Use?

## Admin Site

Once the service is launched, you can visit the admin site by navigating to `/admin` in your browser.
If you deploy using `docker-compose`, a superuser account is already created.
You can find the username and password credentials in the `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD` environment variables.

In the admin site, you can manage departments information, organization roles, and assign employee data to registered users.

## Employee Portal

To access the employee portal, go to `/portal` in your browser.
If a user is not logged in, they will be redirected to the login page. Existing system members can simply log in.
If a user is not yet a system member, they can register a new account by clicking the `Create One!`` button at the bottom of the login page.
