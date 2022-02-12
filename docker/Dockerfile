FROM gitpod/openvscode-server:latest
USER root
RUN apt-get install -y wget
RUN wget https://deb.nodesource.com/setup_16.x
RUN sh setup_16.x
RUN apt-get install -y nodejs
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
WORKDIR /src/
COPY /tiffin_recv ./
COPY entrypoint.sh ./
RUN ln -fs /usr/share/zoneinfo/Asia/Kolkata /etc/localtime
RUN apt-get install -y tzdata
RUN dpkg-reconfigure --frontend noninteractive tzdata
USER openvscode-server
ENTRYPOINT ["sh", "/src/entrypoint.sh"]
# ENTRYPOINT ["bash"]
EXPOSE 8080 3000
