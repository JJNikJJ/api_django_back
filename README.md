# Bike Rental API

## Описание

Проект представляет собой API для аренды велосипедов, построенный с использованием Django и Django REST Framework. В проект включена поддержка задач Celery и Redis для асинхронной обработки задач.

## Требования

- Python 3.12
- Backend: Django, Django Rest Framework
- Асинхронность: Celery
- База данных: PostgreSQL
- Тестирование: PyTest
- Контейнеризация: Docker
- CI/CD: GitLab CI
- 
## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/JJNikJJ/bike_api_django.git
cd bike_api_django
```

### 2. Настройка виртуального окружения и установка зависимостей

```bash
python -m venv .venv
source .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка Docker и Docker Compose

Убедитесь, что у вас установлены Docker и Docker Compose. Затем выполните команду для сборки и запуска контейнеров:

```bash
docker-compose up --build
```

### 4. Применение миграций и создание суперпользователя

Примените миграции и создайте суперпользователя для доступа к административной панели Django:

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 5. Запуск проекта

Для запуска проекта используйте команду:

```bash
docker-compose up
```

Теперь проект должен быть доступен по адресу [http://localhost:8000](http://localhost:8000).

## CI/CD

В проекте настроен CI/CD с использованием GitHub Actions. Скрипты для автоматического тестирования и деплоя находятся в `.github/workflows/`.

## Документация по API

Документация по API доступна по адресу [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

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
