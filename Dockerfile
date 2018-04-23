FROM python:2.7
MAINTAINER "Vincent Bisserie <vbisserie@gmail.com>"

RUN mkdir /srv/app

ENV WORKDIR=/srv/app

WORKDIR $WORKDIR

# Install require software and libraries

COPY ./docker/nginx/nginx.list /etc/apt/sources.list.d/nginx.list
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -

RUN apt-get -y update && \
    apt-get -y install git vim nginx supervisor gettext && \
    apt-get  clean && \
    rm -rf /var/lib/apt/lists/*

# Install common dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    chmod +x /usr/local/bin/uwsgi

COPY ./docker/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY ./docker/supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf
COPY ./docker/supervisor/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf

RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./docker/nginx/site.conf /etc/nginx/conf.d/site.conf

COPY ./docker/uwsgi/uwsgi.ini /etc/uwsgi/uwsgi.ini

COPY ./docker/docker-entrypoint.sh /tmp/docker-entrypoint.sh
COPY . /srv/app

# Application entrypoint
CMD ["/tmp/docker-entrypoint.sh"]