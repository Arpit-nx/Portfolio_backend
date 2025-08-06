FROM python:3.13.5
WORKDIR /backend
COPY ./ backend

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "app.run:app"]