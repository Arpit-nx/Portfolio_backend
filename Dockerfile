# Dockerfile (example for backend at repo root)
FROM python:3.13

WORKDIR /app

COPY backend/ .         

RUN pip install --no-cache-dir -r requirements.txt

# Use sh -c so $PORT is expanded at runtime
CMD ["sh", "-c", "gunicorn run:app --bind 0.0.0.0:$PORT"]
