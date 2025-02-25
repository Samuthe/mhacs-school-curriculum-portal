FROM python:3.9-slim

WORKDIR /app

# Install system dependencies for MySQL & Django dependencies
RUN apt-get update && apt-get install -y \
    mariadb-client \
    libmariadb-dev \
    # mariadb-dev \
    build-essential \
    python3-dev \
    libsqlite3-dev \
    curl \
    ca-certificates \
    gnupg \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Set Django environment variables
ENV DJANGO_SETTINGS_MODULE=studentrecord.settings
ENV PYTHONUNBUFFERED=1

# Create media directory for CKEditor
RUN mkdir -p /app/media/uploads/ckeditor

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Add entrypoint script
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Use entrypoint script to run Django commands
ENTRYPOINT ["/docker-entrypoint.sh"]
