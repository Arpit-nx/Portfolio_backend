FROM python:3.13.5
WORKDIR /backend
COPY ./ backend

RUN pip install -r requirements.txt

CMD ["gunicorn", "app.run:app"]