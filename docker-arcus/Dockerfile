FROM ubuntu:14.04

RUN sed -i 's/archive.ubuntu.com/ftp.kaist.ac.kr/g' /etc/apt/sources.list

RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential autoconf automake libtool libcppunit-dev python-setuptools python-dev \
    ant \
    openjdk-7-jdk \
    libevent-dev

RUN git clone https://github.com/naver/arcus.git
RUN cd arcus/scripts && ./build.sh
# Fix arcus-memcached build issues
RUN cd arcus/server && git checkout develop \
    && ./configure --prefix=/arcus --enable-zk-integration --with-zookeeper=/arcus \
        --with-libevent=/arcus \
    && make && make install

RUN useradd -p arcus -ms /bin/bash arcus
RUN chown -R arcus:arcus /arcus
USER arcus
WORKDIR /arcus/scripts
RUN ./arcus.sh deploy conf/local.sample.json
RUN ./arcus.sh zookeeper init

ADD start.sh /arcus/scripts/start.sh
EXPOSE 11211
CMD /arcus/scripts/start.sh

