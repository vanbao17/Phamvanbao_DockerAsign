# FROM python:3.8-slim
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install  -r requirements.txt
# COPY . /app
# CMD ["python", "app.py"]

FROM python:3
WORKDIR /app
ENV FLASK_APP=app.py
ENV FLASK_ENV=development
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]