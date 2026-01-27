
FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/db

RUN python manage.py collectstatic --noinput || echo "Collectstatic failed, continuing..."


EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000')" || exit 1

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
