#!/bin/bash

# install snap first
yum install -y snapd
systemctl enable --now snapd.socket
ln -sf /var/lib/snapd/snap /snap

# install docker to use with jenkins
snap install docker
groupadd -f docker
chown root:docker /var/run/docker.sock

# enable for jenkins user to use docker
usermod -aG docker jenkins