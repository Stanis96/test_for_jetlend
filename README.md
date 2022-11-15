
  <h3 align="center">Тестовое задание: "Jetlend"
 </h3>

### Используемый стек технологий в задании:
* Django
* DRF
* Pandas
* Celery
* Beautifulsoup
* Poetry
* SQLite3

### Перед запуском выполните:

* Виртуальное окружение:
  ```sh
  poetry config virtualenvs.in-project true
  poetry install
  ```
* В корне проекта создайте ```.env``` и задайте значения переменных:
    ```sh
    DJANGO_SECRET_KEY=
    DEBUG=
    ```
* Cоздание и применение миграции:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```
