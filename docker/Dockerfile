FROM gitpod/openvscode-server:latest
USER root
RUN apt-get install -y wget
RUN wget https://deb.nodesource.com/setup_16.x
RUN sh setup_16.x
RUN apt-get install -y nodejs
WORKDIR /src/
COPY /tiffin_recv ./
COPY entrypoint.sh ./
USER openvscode-server
ENTRYPOINT ["sh", "/src/entrypoint.sh"]
EXPOSE 8080 3000
