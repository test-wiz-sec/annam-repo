FROM golang:1.24-alpine AS build
WORKDIR /src
COPY go.mod ./
COPY *.go ./
RUN CGO_ENABLED=0 go build -o /orders-api .

FROM gcr.io/distroless/static-debian12
COPY --from=build /orders-api /orders-api
EXPOSE 8080
ENTRYPOINT ["/orders-api"]
