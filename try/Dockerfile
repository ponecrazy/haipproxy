FROM vaeum/alpine-python3-pip3

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV ISDOCKER 1
RUN echo -e "http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.7/main/\nhttp://mirrors.tuna.tsinghua.edu.cn/alpine/v3.7/community/" > /etc/apk/repositories
RUN apk upgrade --no-cache \
  && apk add --no-cache \
  python3-dev \
  curl
COPY . /test
WORKDIR /test
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -U pip && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple/ -r requirements.txt
RUN #pip3 install -i https://pypi.douban.com/simple/ -U pip && pip3 install -i https://pypi.douban.com/simple/ -r requirements.txt
#CMD ['python3', 'crawler_booter.py', '--usage', 'crawler', 'common']
