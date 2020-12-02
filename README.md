# Django шаблон для быстрого старта проекта
По дефолту настроено:
* Конфиг settings.py
* Коннект к postgres
* Панель debug_toolbar
* Логирование
* Переменные окружения dotenv 
* Middleware exception handler

Установленные библиотеки:
python-dotenv, psycopg2, django-debug-toolbar, django-debug-toolbar-force

## Installation

Git
```
git clone https://github.com/ymezencev/django_blank_template.git c:/git/application
git remote remove origin
git branch -M main
git remote add origin https://github.com/.../.../.git
git remote -v
git push -u origin main
```
virtual env
```
cd c:\git\application
python -m venv venv
.\venv\Scripts\activate.bat
```
install packages
```
pip install -r requirements.txt
```

postgres
```
psql -U postgres
CREATE DATABASE NAME_DB WITH ENCODING 'UTF8';
GRANT ALL PRIVILEGES ON DATABASE NAME_DB TO dbms;

\c name_db dbms
CREATE EXTENSION pg_trgm;
ALTER EXTENSION pg_trgm SET SCHEMA public;
```

.env
```
создать config/.env и прописать переменные окружения из settings.py
DJANGO_SECRET_KEY=''
DB_NAME=''
DB_USER=''
DB_PASSWD=''
```

django
```
python manage.py runserver
python manage.py startapp new_app_name
 
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
user
password
...
```

