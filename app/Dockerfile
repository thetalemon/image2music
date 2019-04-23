FROM ubuntu:14.04

# 初期設定＆nodeインストール
RUN apt update -y && apt upgrade -y
RUN apt install -y \
    curl \
    nodejs \
    npm \
    git \
    vim \
    fluidsynth
RUN npm cache clean \
 && npm config set strict-ssl false \
 && npm install n -g -y \
 && npm config set strict-ssl t
RUN n stable
RUN ln -sf /usr/local/bin/node /usr/bin/node
RUN apt purge nodejs npm -y

# node
RUN mkdir /var/www/
WORKDIR /var/www
COPY ./src/vue ./
RUN npm install
RUN npm run build

# python関係
ENV PYTHON_VERSION 3.6.0
ENV HOME /root
ENV PYTHON_ROOT $HOME/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT $HOME/.pyenv
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
RUN $PYENV_ROOT/plugins/python-build/install.sh
RUN /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT
RUN rm -rf $PYENV_ROOT

WORKDIR /var/www/
COPY requirements.txt /var/www
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY run.py /var/www
COPY uwsgi.ini /var/www
COPY functions /var/www/functions

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
