FROM python:2.7
MAINTAINER renu joshi "renujoshi333@gmail.com"
COPY ./flaskweb/ /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE 8080

FROM mysql

ENV MYSQL_DATABASE restpython

COPY ./mysql/ /docker-entrypoint-initdb.d/
EXPOSE 3306
