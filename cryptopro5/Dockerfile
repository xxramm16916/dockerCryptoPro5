# Базовый образ с КриптоПро
FROM debian:latest as cryptopro-generic

ADD scripts /scripts
ADD dist /tmp/src

# Устанавливаем timezone
ENV TZ="Europe/Moscow" \
    docker="1"

# Установка зависимостей.
RUN apt-get -y update 
#RUN apt-get -y install cmake build-essential libboost-all-dev python3-dev unzip mc net-tools

# Установка КриптоПРО CSP.
RUN cd /tmp/src && \
	tar zxf linux-amd64_deb.tgz && \
	cd linux-amd64_deb && \
	./install.sh && \
	apt -y install ./lsb-cprocsp-devel_5.0.12330-6_all.deb
	
# Установка КриптоПРО ЭЦП CSP.
RUN cd /tmp/src && \
	tar xzf cades-linux-amd64.tar.gz && \
	#cd cades-linux-amd64 && \
	apt -y install ./cprocsp-pki-cades-64_2.0.14458-1_amd64.deb

# Установка симлинков
RUN cd /bin && \
    ln -s /opt/cprocsp/bin/amd64/certmgr && \
    ln -s /opt/cprocsp/bin/amd64/cpverify && \
    ln -s /opt/cprocsp/bin/amd64/cryptcp && \
    ln -s /opt/cprocsp/bin/amd64/csptest && \
    ln -s /opt/cprocsp/bin/amd64/csptestf && \
    ln -s /opt/cprocsp/bin/amd64/der2xer && \
    ln -s /opt/cprocsp/bin/amd64/inittst && \
    ln -s /opt/cprocsp/bin/amd64/wipefile && \
    ln -s /opt/cprocsp/sbin/amd64/cpconfig	

ADD app /app

# Установка python
RUN apt-get install -y python3-pip
RUN pip install flask
RUN pip install python-dotenv

#ENTRYPOINT ['python3']
#CMD ['python3', '/app/app.py']

EXPOSE 5000