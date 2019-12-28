FROM python:3.9.0a2-alpine3.10
RUN pip install Flask
WORKDIR /usr/src/flaskapp
COPY ./app.py ./
RUN mkdir /var/log/example5
VOLUME /var/log/example5
CMD python app.py