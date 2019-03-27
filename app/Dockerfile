FROM node:6.11.3-alpine AS build-stage

RUN mkdir /var/www
WORKDIR /var/www
COPY ./ ./

WORKDIR /var/www/src/vue

RUN npm install
RUN npm install axios
RUN npm run build

FROM python:3.6

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /var/www/

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
