===============

Jenkins Docker

Dind (Docker in Docker)
> Docker Container가 Docker Daemon 탑재
> Docker Container 안의 Docker Daemon이 또다른 Docker Container들을 기동
> Docker Container는 Privileged 권한이 필요함 (보안적으로 취약함)

DooD (Docker out of Docker)
> Docker Container가 Docker Clinet 탑재
> Docker Container 안의 Docker Client가 Docker Host의 Docker Daemon과 통신
> Docker Client가 띄운 Container는 Docker Host에 기동됨
> 통신 방법으로는 /var/run/docker.sock or TLS 방식이 있음
> /var/run/docker.sock을 이용할 땐 Jenkins Container안의 Jenkins User에 접근권한을 부여할 수 있도록 Docker Host의 Docker group ID를 그대로 Jenkins Container안에 추가하고, Jenkins User를 Docker Group에 추가해야함

===============

agent:
- none
- any
- label
- node
- docker
- dockerfile
- kubernetes

agent { label 'service || batch' }
agent { label 'service && batch' }
agent { label 'service' }
agent { label 'batch' }

post:
- always
- changed
- fixed
- regression
- aborted
- failure
- success
- unstable
- unsuccessful
- cleanup

parameters:
- string
- text
- booleanParam
- choice
- password

===============

