
В рамках проекта вам необходимо создать веб-приложение на Django,
которое позволяет пользователям управлять рассылками сообщений для клиентов.
Приложение должно включать функциональность для:
- создания;
- просмотра;
- редактирования и удаления рассылок;
- отправки сообщений по требованию.

## Установка:

1. Клонируйте репозиторий:
https://github.com/MaratZ
## Конфигурация
1. Создайте виртуальное окружение poetry.

```
poetry env
```

2. Установите библиотеки Flake8, black, isort, mypy в группу lint.

```commandline
poetry add --group lint flake8
poetry add --group lint black
poetry add --group lint isort
poetry add --group lint mypy
```

3. Создайте файл .flake8 для настройки библиотеки flak8


4. Настройте установленные библиотеки, используя кода ниже

Файл .flake8

```
[flake8]
max-line-length = 119
```

5. Установите требуемые библиотеки:
````commandline
poetry add requests
poetry add python-dotenv
poetry add psycopg2
poetry add django
poetry add redis
````

6. Инициализируйте django-проект внутри текущей директории
````
django-admin startproject config .
````


## Приложение по рассылки сообщений:

1. Создайте приложение mailing
````
python manage.py startapp mailing
````
2. Зарегистрируйте приложение в settings.py