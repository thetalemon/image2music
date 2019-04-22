FROM ubuntu:14.04
RUN apt update -y
RUN apt upgrade -y
RUN apt-get install -y curl
RUN apt install -y nodejs npm
RUN npm cache clean
RUN npm config set strict-ssl false
RUN npm install n -g -y
RUN npm config set strict-ssl t
RUN n stable
RUN ln -sf /usr/local/bin/node /usr/bin/node
RUN node -v
RUN apt purge nodejs npm -y
RUN node -v

RUN mkdir /var/www/
WORKDIR /var/www
COPY ./src/vue ./
RUN ls -l
RUN npm install
RUN npm install axios
RUN npm run build

ENV PYTHON_VERSION 3.6.0
ENV HOME /root
ENV PYTHON_ROOT $HOME/local/python-$PYTHON_VERSION
ENV PATH $PYTHON_ROOT/bin:$PATH
ENV PYENV_ROOT $HOME/.pyenv
RUN apt-get update && apt-get upgrade -y \
 && apt-get install -y \
    git \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev
RUN git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
RUN $PYENV_ROOT/plugins/python-build/install.sh
RUN /usr/local/bin/python-build -v $PYTHON_VERSION $PYTHON_ROOT
RUN rm -rf $PYENV_ROOT

RUN python -V

WORKDIR /var/www/
COPY requirements.txt /var/www

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y fluidsynth

RUN ls -l

COPY run.py /var/www
COPY uwsgi.ini /var/www
COPY functions /var/www/functions

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
