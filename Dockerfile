FROM alpine:3.14

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV ISDOCKER 1

RUN echo -e "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.14/main/\nhttp://mirrors.tuna.tsinghua.edu.cn/alpine/v3.14/community/" > /etc/apk/repositories
RUN apk upgrade --no-cache
RUN apk add --no-cache \
  squid \
  python3-dev \
  libffi-dev \
  curl \
  wget \
  g++

#  libxml2-dev \
#  libxml2 \
#  libxslt-dev \
#  libxslt

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

#RUN apt update
#RUN apt install squid -yq
RUN sed -i 's/http_access deny all/http_access allow all/g' /etc/squid/squid.conf && cp /etc/squid/squid.conf /etc/squid/squid.conf.backup
#RUN apt install python3 python3-pip -yq
#RUN which python3|xargs -i ln -s {} /usr/bin/python
#RUN which pip3|xargs -i ln -s {} /usr/bin/pip
COPY . /haipproxy
WORKDIR /haipproxy
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -U pip && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
RUN #pip3 install -i https://pypi.douban.com/simple/ -U pip && pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt
#CMD ['python3', 'crawler_booter.py', '--usage', 'crawler', 'common']

