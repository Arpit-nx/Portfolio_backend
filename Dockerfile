FROM python:3.13.5

WORKDIR /app

COPY backend/ .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "run:app"]
