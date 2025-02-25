FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libsqlite3-dev \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=portfolio.settings
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /app/media/uploads/ckeditor


RUN python manage.py makemigrations
RUN python manage.py migrate

RUN python manage.py create_superuser

EXPOSE 8000

CMD sh -c "python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:8000 studentrecord.wsgi:application"

# CMD ["sh", "-c", "python manage.py migrate && ["gunicorn", "--bind", "0.0.0.0:8000", "portfolio.wsgi:application"]