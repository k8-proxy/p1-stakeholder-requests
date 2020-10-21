
# Dockerfile for c-icap-client

## How to build a docker image

```sh
docker build -t c-icap-client .
```

## How to run a docker container

```sh
docker run c-icap-client <c-icap-client options>
```

NOTE: You should run `c-icap` docker container before running `c-icap-client`.

```sh
docker run -p 1344:1344 c-icap
```
