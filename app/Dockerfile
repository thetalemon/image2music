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

# WORKDIR /
# RUN apk --update --no-cache add \
#     build-base \
#     openssl \
#     musl \
#     linux-headers \
#     make \
#     git \
#     python3
# RUN wget "https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz"
# RUN tar xzvf Python-3.5.2.tgz
# WORKDIR /Python-3.5.2
# RUN ls -l
# RUN ./configure
# RUN make
# RUN make install
# RUN python3 -V


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

# WORKDIR /
# RUN sudo apt-get install -y git
# RUN sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
#   libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
#   xz-utils tk-dev libffi-dev liblzma-dev
# RUN git clone https://github.com/yyuu/pyenv.git /pyenv
# WORKDIR /pyenv/plugins/python-build
# RUN ./install.sh
# RUN /usr/local/bin/python-build -v 3.7.1 ~/local/python-3.7.1
# WORKDIR /
# RUN rm -rf /pyenv
# RUN pyenv global 3.6.0
RUN python -V


# FROM python:3.6

# ENV LANG C.UTF-8
# ENV TZ Asia/Tokyo

# RUN mkdir -p /var/www/
WORKDIR /var/www/
COPY requirements-local.txt /var/www
#
# RUN python3 -V
# RUN ls -l
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements-local.txt
RUN apt-get update && apt-get install -y fluidsynth

RUN ls -l

COPY run.py /var/www
COPY uwsgi.ini /var/www
COPY functions /var/www/functions
# COPY --from=build-stage /app/dist /var/www/dist

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]
