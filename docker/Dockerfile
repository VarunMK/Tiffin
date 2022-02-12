FROM ubuntu:latest
RUN apt update
RUN apt install -y git python3 python3-pip 
RUN apt install -y build-essential
RUN apt install -y curl
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    echo 'deb https://deb.nodesource.com/node_14.x focal main' \
    > /etc/apt/sources.list.d/nodesource.list
RUN curl -s https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo 'deb https://dl.yarnpkg.com/debian/ stable main' \
    > /etc/apt/sources.list.d/yarn.list
RUN apt update
RUN apt install -y nodejs yarn
RUN npm config set python python3
RUN npm install -g code-server@4.0.2 --unsafe-perm
EXPOSE 8080
CMD ["bash"]