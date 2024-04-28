# django_boilerplate_no_drf
Simple Django Boilerplate Code (Without DRF)

### Directory Structure:
    - authentication (app)
    - core (main project)
    - static
    - templates
    - .env (you have to create this file manually)
    - .gitignore
    - manage.py
    - README.md
    - requirements.txt

### Steps to Run the Project Locally
- Clone the repo: `git clone https://github.com/pintuprajapati/django_boilerplate_no_drf.git`
    - You can change the name of the folder from `django_boilerplate_no_drf` to `anything you want`.
- Create a virtual envrionment (venv): `python3 -m venv venv`
- Activate venv: 
    - In Linux: `source venv/bin/activate`
    - In Windows: `source venv/Scripts/activate`
- Install dependencies: `pip3 install -r requirements.txt`
- Set Up Environment Variables
    - Create a `.env` file in the project root directory
    - I have metioned what you can define in .env file below. Just copy and paste.
- Database Migrations:
    - Generate database migration files: `python3 manage.py makemigrations`
    - Apply database migrations: `python3 manage.py migrate`
    - Create superuser to access admin: `python3 manage.py createsuperuser`
- Run the server: `python3 manage.py runserver`
- To go to admin panel: `http://127.0.0.1:8000/your-secret-admin-url-from-.env-file`


### .env file (Define the following environment variables)
```
DJANGO_SECRET_KEY=<your_django_secret_key>
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost
DJANGO_SECRET_ADMIN_URL=<your_secret_admin_url>

# postgres db
PG_DB_NAME=<your_postgres_db_name>
PG_DB_USER=<your_postgres_db_user>
PG_DB_PASS=<your_postgres_db_password>
PG_DB_HOST=<your_postgres_db_host>
PG_DB_PORT=<your_postgres_db_port>
```
