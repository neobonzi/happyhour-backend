FROM ubuntu:16.04
MAINTAINER Chris Brantley

# Install PostgreSQL
RUN apt-get update
RUN apt-get install -y postgresql-9.5 postgresql-contrib-9.5 postgis

# Update config to allow remote connections
RUN echo "host all all 0.0.0.0/0 trust" >> /etc/postgresql/9.5/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf

# restart
RUN service postgresql restart

# switch to the postgres user
USER postgres

# Expose the PostgreSQL port
EXPOSE 5432

# Create root superuser
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER root WITH SUPERUSER PASSWORD 'password';" &&\
    createdb happyhour &&\
    psql happyhour --command "CREATE EXTENSION postgis;"

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/9.5/bin/postgres", "-D", "/var/lib/postgresql/9.5/main", "-c", "config_file=/etc/postgresql/9.5/main/postgresql.conf"]

