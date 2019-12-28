FROM node:10.18.0-alpine3.10
USER node
WORKDIR /home/node
COPY --chown=node:node ../../app app
#COPY --chown=node:node app app
WORKDIR /home/node/app
RUN npm install
EXPOSE 3000
CMD npm start
