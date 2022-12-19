FROM jenkins/jenkins:lts
ARG DOCKER_GID
USER root

# install docker client
RUN apt-get update && apt-get install -y lsb-release && apt-get clean
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
    signed-by=/etc/apt/keyrings/docker.gpg] \
    https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli

# set jenkins user to host docker group
RUN /usr/sbin/groupadd -g ${DOCKER_GID} -f docker && \
    /usr/sbin/usermod -aG docker jenkins

USER jenkins