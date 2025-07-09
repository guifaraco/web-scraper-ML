FROM python:3.12-slim

ENV UV_SYSTEM_PYTHON=true

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync

COPY . .

CMD ["python", "scraper/main.py"]