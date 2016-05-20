FROM ubuntu:14.04

RUN sed -i 's/archive.ubuntu.com/ftp.kaist.ac.kr/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    git \
    build-essential python-dev \
    python3 python3-pip \
    librrd-dev rrdtool

RUN pip3 install kazoo psutil rrdtool django

RUN git clone https://github.com/naver/hubblemon.git

ADD settings.patch /hubblemon/settings.patch
RUN cd hubblemon && git apply settings.patch

VOLUME /log
ADD start.sh /start.sh
CMD ["/bin/bash", "/start.sh"]
