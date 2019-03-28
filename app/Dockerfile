FROM node:lts-alpine as build-stage

RUN mkdir /app
WORKDIR /app
COPY ./src/vue ./

WORKDIR /app

RUN npm install
RUN npm install axios
RUN npm run build

FROM python:3.6

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

WORKDIR /var/www/
RUN mkdir /var/www/vue/

COPY --from=build-stage /app /var/www/vue
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
