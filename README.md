# Bike API Django Project

## Описание проекта

Это проект Bike API, разработанный на Django, который предоставляет REST API для управления арендами велосипедов. Проект использует Docker для контейнеризации всех сервисов и GitHub Actions для CI/CD.

## Содержание

- [Bike API Django Project](#bike-api-django-project)
  - [Описание проекта](#описание-проекта)
  - [Требования](#требования)
  - [Установка](#установка)
  - [Запуск проекта](#запуск-проекта)
  - [API Документация](#api-документация)
  - [CI/CD](#cicd)
  - [Примеры запросов для тестирования API](#примеры-запросов-для-тестирования-api)

## Требования

- Docker
- Docker Compose
- Git
- Python 3.12

## Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/JJNikJJ/api_django_back.git
   cd api_django_back
   ```

2. Создайте виртуальное окружение и установите зависимости:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Запуск проекта

1. Запустите все сервисы с помощью Docker Compose:
   ```sh
   docker-compose up --build
   ```

2. Выполните миграции и создайте суперпользователя:
   ```sh
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py createsuperuser
   ```

3. Откройте браузер и перейдите по адресу [http://localhost:8000](http://localhost:8000).

## API Документация

API документация автоматически генерируется с использованием Swagger и доступна по адресу [http://94.26.250.140:8000/swagger/](http://94.26.250.140:8000/swagger/).

## CI/CD

В проекте настроен CI/CD с использованием GitHub Actions. Скрипты для автоматического тестирования и деплоя находятся в `.github/workflows/`.

## Примеры запросов для тестирования API

### 1. Регистрация пользователя

**Запрос:**

```bash
curl -X POST http://localhost:8000/api/users/ -d '{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "testpassword123"
}'
```

**Ответ:**

```json
{
  "id": 1,
  "username": "testuser",
  "email": "testuser@example.com"
}
```

### 2. Получение токена

**Запрос:**

```bash
curl -X POST http://localhost:8000/api/token/ -d '{
  "username": "testuser",
  "password": "testpassword123"
}'
```

**Ответ:**

```json
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### 3. Список велосипедов

**Запрос:**

```bash
curl -X GET http://localhost:8000/api/bikes/ -H "Authorization: Bearer <your_access_token>"
```

**Ответ:**

```json
[
  {
    "id": 1,
    "name": "Bike 1",
    "description": "Description 1",
    "is_available": true
  },
  {
    "id": 2,
    "name": "Bike 2",
    "description": "Description 2",
    "is_available": true
  }
]
```

### 4. Аренда велосипеда

**Запрос:**

```bash
curl -X POST http://localhost:8000/api/rentals/1/rent/ -H "Authorization: Bearer <your_access_token>"
```

**Ответ:**

```json
{
  "status": "Bike rented",
  "rental_id": 1
}
```

### 5. Возврат велосипеда

**Запрос:**

```bash
curl -X POST http://localhost:8000/api/rentals/1/return_bike/ -H "Authorization: Bearer <your_access_token>"
```

**Ответ:**

```json
{
  "status": "Bike returned"
}
```
