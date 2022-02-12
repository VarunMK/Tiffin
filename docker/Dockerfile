FROM ubuntu:latest
RUN curl -fsSL https://deb.nodesource.com/setup_17.x | bash -
RUN apt update
RUN apt install -y git python3 python3-pip nodejs
RUN apt install -y build-essential pkg-config
RUN apt install -y curl
RUN npm config set python python3
RUN npm install -g code-server@4.0.2
EXPOSE 8080
CMD ["code-server"]