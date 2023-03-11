# yamdb_final
yamdb_final
https://github.com/v-mcsimoff/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg
### Описание проекта
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории:«Книги», «Фильмы», «Музыка». Список категорий может быть расширен (например, можно добавить категорию «Картины» или «Ювелирные изделия»). Произведению может быть присвоен жанр из списка предустановленных (например, «Легенда», «Поп» или «Триллер»). Администратор может добавлять произведения, категории и жанры. 
Пользователи оставляют к произведениям отзывы и ставят произведению оценку в диапазоне от 1 до 10; из пользовательских оценок формируется рейтинг. Пользователь может оставить только один отзыв на одно произведение. Пользователи могут оставлять комментарии к отзывам.
Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.

### Используемый стек:
Python 3.10, Django 3.2, DRF 3.12, JWT, DJOSER, SQLite
### Как запустить проект:
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/v-mcsimoff/yamdb_final.git
cd yamdb_final
cd api_yamdb
```

Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source /venv/bin/activate
python -m pip install --upgrade pip
```

Ставим зависимости из requirements.txt:
```bash
pip install -r requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

Поднимаем контейнеры (db, web, nginx):
```bash
docker-compose up -d --build
```

Выполняем миграции:
```bash
docker-compose exec web python manage.py makemigrations reviews
```
```bash
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:
```bash
docker-compose exec web python manage.py createsuperuser
```

Србираем статику:
```bash
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп базы данных (нет в текущем репозитории):
```bash
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Шаблон наполнения .env, расположенный по пути infra/.env
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Документация API YaMDb
Документация доступна по эндпойнту: http://localhost/redoc/
Автор: <br>[Владимир](https://github.com/v-mcsimoff)