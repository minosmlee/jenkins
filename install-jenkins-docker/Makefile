DOCKER_GID := $(shell getent group docker | awk -F: '{print $$3}')
IMAGE := jenkins
TAG := v1
SERVICE := jenkins

export IMAGE
export TAG
export SERVICE

build:
        docker-compose build
run:
        docker-compose up -d
destroy:
        docker-compose down
ps:
        docker ps -a --no-trunc
log:
        docker logs $(SERVICE)
exec:
        docker exec -it $(SERVICE) /bin/bash