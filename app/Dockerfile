FROM node:lts-alpine as build-stage

RUN mkdir /app
WORKDIR /app
COPY ./src/vue ./

RUN npm install
RUN npm install axios
RUN npm run build

FROM python:3.6

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN mkdir -p /var/www/
WORKDIR /var/www/
COPY requirements.txt /var/www
RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY run.py /var/www
COPY uwsgi.ini /var/www
COPY functions /var/www/functions
COPY --from=build-stage /app/dist /var/www/dist

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
