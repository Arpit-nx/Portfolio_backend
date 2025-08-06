# Dockerfile (repo root)
FROM python:3.13

WORKDIR /app

# Copy everything from repo root into /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use the correct gunicorn entry:
# If run.py is at repo root and defines "app", use run:app
CMD ["gunicorn", "run:app", "--bind", "0.0.0.0:$PORT"]
