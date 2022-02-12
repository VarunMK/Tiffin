FROM node:17-slim
# ports and volumes
RUN mkdir -p /src/tfnrcv /src/dev
COPY tiffin_recv/ /src/tfnrcv
COPY entrypoint.sh /src
WORKDIR /src/dev
CMD ["sh", "/src/entrypoint.sh"]