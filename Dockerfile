# Файл: ~/web_interface_db/Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

ENV PYTHONPATH /app

# Исправленная команда запуска
CMD ["gunicorn", "--bind", "0.0.0.0:8001", "--log-level", "debug" ,"core.wsgi:application"]
