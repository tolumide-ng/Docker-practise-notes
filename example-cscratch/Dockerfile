FROM alpine:3.7 as builder
WORKDIR /root/
COPY example.c .
RUN apk --update --no-cache add build-base && gcc -static -o example example.c
FROM scratch
COPY --from=builder /root/example /
ENTRYPOINT ["/example"]
CMD ["World"]



# docker build -t tolumides/example-cscratch:1.0 .