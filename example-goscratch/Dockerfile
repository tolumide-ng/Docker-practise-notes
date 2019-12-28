FROM golang:1.10.0 as builder
WORKDIR /go/src/app
COPY example.go /
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o example example.go

FROM scratch
COPY --from=builder /go/src/app/example /
ENTRYPOINT [ "/example" ]