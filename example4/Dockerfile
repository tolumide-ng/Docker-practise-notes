FROM alpine:3.7
RUN adduser -D example4
USER example4
WORKDIR /home/example4/bin
COPY --chown=example4:example4 ./setup.sh ./myscript.sh ./
RUN chmod 764 ./setup.sh ./myscript.sh
ENV script_env=dev
ENTRYPOINT ["./setup.sh"]
CMD ["World"]