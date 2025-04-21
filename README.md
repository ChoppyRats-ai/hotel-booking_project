# Hotel Booking API

REST API для системы бронирования отелей. Позволяет управлять комнатами и бронированиями.

## Требования

- Docker
- Docker Compose

## Быстрый старт

1. Клонировать репозиторий:
```bash
git clone <url-репозитория>
cd <папка-проекта>
```

2. Создать файл окружения:
```bash
cp .env.example .env
```

3. Запустить проект:
```bash
docker-compose up -d
```

API будет доступно по адресу: http://localhost:8000/api/v1/

## API Endpoints

### Комнаты
- `GET /api/v1/rooms/` - список всех комнат
- `POST /api/v1/rooms/` - создать комнату
- `GET /api/v1/rooms/{id}/` - детали комнаты
- `PUT /api/v1/rooms/{id}/` - обновить комнату
- `DELETE /api/v1/rooms/{id}/` - удалить комнату

### Бронирования
- `GET /api/v1/bookings/` - список бронирований
- `POST /api/v1/bookings/` - создать бронирование
- `GET /api/v1/bookings/{id}/` - детали бронирования
- `PUT /api/v1/bookings/{id}/` - обновить бронирование
- `DELETE /api/v1/bookings/{id}/` - удалить бронирование

## Команды Docker

```bash
# Запустить проект
docker-compose up -d

# Остановить проект
docker-compose down

# Посмотреть логи
docker-compose logs -f

# Пересобрать и запустить (если были изменения)
docker-compose up -d --build

# Применить миграции
docker-compose exec api python src/manage.py migrate

# Создать суперпользователя
docker-compose exec api python src/manage.py createsuperuser
```

## Разработка

1. Установить зависимости для разработки:
```bash
poetry install
```

2. Запустить тесты:
```bash
poetry run pytest
```

3. Запустить линтер:
```bash
poetry run ruff .
```

## Структура проекта

├── src/
│ ├── hotel/ # основные настройки проекта
│ ├── hotelbooking/ # приложение для бронирования
│ └── manage.py
├── tests/ # тесты
├── docker-compose.yml
├── Dockerfile
├── pyproject.toml 
└── README.md