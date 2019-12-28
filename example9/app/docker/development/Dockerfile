FROM tolumide/example9:9.1.0
USER root
RUN npm install -g nodemon
USER node
ENV DEBUG="app:* npm start"
CMD nodemon bin/www



# docker build ct tolumide/example9:dev -f docker/development/Dockerfile .