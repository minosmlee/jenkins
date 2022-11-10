#!/bin/bash

# install docker to use with jenkins
yum install -y docker
systemctl enalbe --now docker
groupadd -f docker
chown root:docker /var/run/docker.sock

# enable for jenkins user to use docker
usermod -aG docker jenkins