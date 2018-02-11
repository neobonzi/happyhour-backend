FROM ubuntu:14.04
MAINTAINER James Bilous

run apt-get update
run apt-get install -y nginx vim inotify-tools

COPY nginx.conf /etc/nginx/nginx.conf
COPY runserver.sh /

RUN chmod a+x /runserver.sh

EXPOSE 80
CMD ["/runserver.sh"]
