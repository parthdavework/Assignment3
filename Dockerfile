FROM python:3.7
ENV FLASK_APP=app

LABEL version="1.0.0"
LABEL description="This is Flask api assignment project"
LABEL maintainer = ["parthdave.work@gmail.com"]

# Set working directory

WORKDIR /usr/src/flask-backend

RUN pip3 install pipenv
RUN pip3 install flask
RUN pip3 install flask-cors
RUN pip3 install flask-mysql
RUN pip3 install mysql-connector-python
RUN pip3 install sqlalchemy
RUN pip3 install psycopg2

COPY . .

# RUN flask --app api_v1 run -p 5060
CMD ["python3","-m","flask","run","--host=0.0.0.0","-p 5060"]
EXPOSE 5060
EXPOSE 3306
# RUN pipenv run python api/app_v1.py