FROM python:2.7
MAINTAINER "Vincent Bisserie <vbisserie@gmail.com>"

RUN mkdir /srv/app

ENV WORKDIR=/srv/app

WORKDIR $WORKDIR

# Install require software and libraries

COPY ./docker/nginx.list /etc/apt/sources.list.d/nginx.list
RUN curl http://nginx.org/keys/nginx_signing.key | apt-key add -

RUN apt-get -y update && \
    apt-get -y install git vim nginx supervisor gettext && \
    apt-get  clean && \
    rm -rf /var/lib/apt/lists/*

# Install common dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
    chmod +x /usr/local/bin/uwsgi

COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY ./docker/supervisord.conf /etc/supervisor/supervisord.conf
RUN rm /etc/nginx/conf.d/default.conf

# Create nginx temporary folders.
RUN mkdir -p /tmp/nginx /tmp/app/logs && chown -R www-data: /tmp/nginx /tmp/app/logs

COPY ./docker/site.conf /etc/nginx/conf.d/site.conf
COPY ./docker/uwsgi.conf /etc/supervisor/conf.d/uwsgi.conf
COPY . /srv/app

# Application entrypoint
CMD ["/srv/app/docker/docker-entrypoint.sh"]