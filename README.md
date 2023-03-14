<h2 align="center">BUfet site</h2>


### Описание проекта:
Другой сайт для Буфета


### Инструменты разработки

**Стек:**
- Python >= 3.10
- Django >=  4.0.4
- sqlite3

## Разработка

##### 1) Сделать форк репозитория и поставить звездочку)

##### 2) Клонировать репозиторий

    git clone ссылка_сгенерированная_в_вашем_репозитории

##### 3) Создать виртуальное окружение

    python -m venv venv
    
##### 4) Активировать виртуальное окружение

##### 5) Устанавливить зависимости:

    pip install -r requirements.txt

##### 6) Выполнить команду для выполнения миграций

    python manage.py migrate
    
##### 7) Создать суперпользователя

    python manage.py createsuperuser
    
##### 8) Залейте тестовіе данніе в бд из fixture

    pip install django_dump_load_utf8
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/category.json
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/tags.json
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/post.json
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/recipe.json
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/comment.json
    python.exe -Xutf8 .\manage.py loaddata blog/fixture/newsletter.json

##### 9) Запустить сервер

    python manage.py runserver


Copyright (c) 2022-present, KoT - Chebanov Konst



