FROM python:3.12.2-bookworm

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install flask
RUN pip install gunicorn
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["gunicorn", "--bind", "127.0.0.1:8000", "wsgi:app"]