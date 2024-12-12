#LeadHit Test Case

Сервис управления формами.

<details><summary><h2>Реализованые возможности</h2></summary>
- Добавление новой формы в базу данных.
- Получение одной соответствующей запросу формы.
- Получение списка форм соответствующих запросу.
</details>

<details><summary><h2>Запуск проекта</h2></summary>
1. Клонируйте репозиторий, создайте виртуальное окружение и активируйте его.

2. Установите poetry:
```bash
pip install poetry
```
3. Установите зависимости:
```bash
poetry install
```
Можно использовать ключ "--only main", если не нужно запускать тесты или линтеры.

4. Создайте .env файл с данными для подключения к бд:
```
MONGO_INITDB_ROOT_USERNAME = mongo_user
MONGO_INITDB_ROOT_PASSWORD = secret_password
```
5. Все настройки приложения находятся в файле src/config/config.yaml. Измените значение db_hostname на "localhost".

6. Базу данных можно запустить в контейнере:
```bash
docker compose -f .\docker-compose-dev.yaml up -d
```
7. Запустите приложение:
```bash
export PYTHONPATH=src/
```
```bash
uvicorn src.app.main:app --reload
```
Либо используйте:
```bash
python main.py
```

Документация будет доступна по адресу: http://127.0.0.1:8000/docs
</details>

<details><summary><h2>Запуск проекта через докер</h2></summary>

1. Создайте .env файл с данными для подключения к бд:
```
MONGO_INITDB_ROOT_USERNAME = mongo_user
MONGO_INITDB_ROOT_PASSWORD = secret_password
```
2. Скопируйте файл docker-compose-prod.yaml в директорию с .env файлом.

3. Выполните команду:
```bash
docker compose -f .\docker-compose-prod.yaml up -d
```

Документация будет доступна по адресу: http://127.0.0.1:8000/docs
</details>

<details><summary><h2>Запуск проекта через докер без загрузки образа.</h2></summary>

1. Клонируйте репозиторий, создайте виртуальное окружение и активируйте его.

2. Создайте .env файл с данными для подключения к бд:
```
MONGO_INITDB_ROOT_USERNAME = mongo_user
MONGO_INITDB_ROOT_PASSWORD = secret_password
```
3. Все настройки приложения находятся в файле src/config/config.yaml.

4. Запустите приложение:
```bash
docker compose up -d
```
