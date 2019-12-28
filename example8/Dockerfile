FROM node:10.18.0-alpine3.10
USER node
RUN mkdir /home/node/app
WORKDIR /home/node/app
COPY --chown=node:node package*.json index.js ./
RUN npm install
EXPOSE 3000
CMD node index.js
