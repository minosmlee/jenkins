#!/bin/bash

# install jenkins
wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum install epel-release
yum install -y jenkins java-11-openjdk-devel
systemctl enable --now jenkins

# install docker to use with jenkins
yum install -y docker
systemctl enalbe --now docker
groupadd -f docker
chown root:docker /var/run/docker.sock

# enable for jenkins to use docker
usermod -aG docker jenkins