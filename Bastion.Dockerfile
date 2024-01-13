FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y gnupg wget iputils-ping && \
    wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | tee /etc/apt/trusted.gpg.d/server-7.0.asc && \
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list && \
    apt-get update && \
    apt-get install -y mongodb-mongosh && \
    echo 'alias mongo="mongosh mongodb://mongodb:27017/people"' >> /root/.bashrc
