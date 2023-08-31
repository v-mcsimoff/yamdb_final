# YaMDb
![yamdb_final](https://github.com/v-mcsimoff/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)
### Project description
The YaMDb project gathers users' reviews of creative works. The works are divided into categories: "Books", "Movies", and "Music". The list of categories can be extended (for example, you can add the categories "Paintings" or "Jewelry"). A work can be assigned a genre from the list of preset genres (for example, "Legend", "Pop" or "Thriller"). The administrator can add works, categories and genres. 
Users post reviews for works and rate the work from 1 to 10; user evaluations are used to calculate a rating. A user can post only one review per work. Users can comment on reviews.
Only authenticated users can add reviews, comments and rate works.

### Technologies:
Python 3.10, Django 3.2, DRF 3.12, JWT, DJOSER, SQLite
### How to launch the project:
Clone the repository and access it:
```bash
git clone https://github.com/v-mcsimoff/yamdb_final.git
cd yamdb_final
cd api_yamdb
```

Create and activate the virtual environment:
```bash
python3 -m venv venv
source /venv/bin/activate
python -m pip install --upgrade pip
```

Install dependencies from requirements.txt:
```bash
pip install -r requirements.txt
```

Access the folder with the file docker-compose.yaml:
```bash
cd infra
```

Build containers (db, web, nginx):
```bash
docker-compose up -d --build
```

Perform migrations:
```bash
docker-compose exec web python manage.py makemigrations reviews
```
```bash
docker-compose exec web python manage.py migrate
```

Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

Collect static files:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Create a database dump (there is no database dump in the current repository):
```bash
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Stop the containers:
```bash
docker-compose down -v
```

### The .env content template located at the infra/.env path
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Documentation API YaMDb
Documentation is available at the endpoint: http://localhost/redoc/

Author: <br>[Vladimir Maksimov](https://github.com/v-mcsimoff) 
