FROM python:3.8

ENV VERSION 0.1.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /{code,files,static}

#USER www-data
ENV PATH /var/www/.local/bin:${PATH}


WORKDIR /code

ENV DEBUG=False
ENV SECRET_KEY=superSecretKey

COPY . /code/

RUN apt-get update && apt-get install -y unixodbc-dev freetds-dev freetds-bin tdsodbc
RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt




VOLUME /static

EXPOSE $PORT
CMD gunicorn --bind 0.0.0.0:$PORT stx.wsgi
#CMD exec gunicorn ng.wsgi:application - --bind 0.0.0.0:8000
