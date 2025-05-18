# Dockerfile
FROM python:3.13-slim

# Install Poetry
RUN pip install --no-cache-dir poetry

WORKDIR /app

# Copy only pyproject.toml and poetry.lock first (for better caching)
COPY pyproject.toml poetry.lock* ./

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

# Copy app source
COPY ./src ./src
WORKDIR /app/src

CMD ["python", "main.py"]
