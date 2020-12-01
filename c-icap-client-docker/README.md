
# Dockerfile for c-icap-client

## How to build a docker image

```sh
$ sudo docker build -t c-icap-client .
```

## How to run a docker container

NOTE: You should run `c-icap-server` docker container before running `c-icap-client`. You can build it from [here](https://github.com/filetrust/c-icap).

```sh
$ sudo docker run -p 1344:1344 c-icap-server
```

Then `c-icap-server` docker container will run on `1344` port and you may run `c-icap-client` as the following syntax.

```sh
$ sudo docker run -v <Host folder>:<Docker container folder> --network host c-icap-client <c-icap-client options>
```

For example, you may use the following command to filter `/opt/test.mp4` file using `gw_rebuild` service of `c-icap-server`.

```sh
$ sudo docker run -v /opt:/opt --network host c-icap-client -s gw_rebuild -f /opt/test.mp4 -o /tmp/test_out.mp4 -v
ICAP server:localhost, ip:127.0.0.1, port:1344

No modification needed (Allow 204 response)

ICAP HEADERS:
	ICAP/1.0 204 Unmodified
	Server: C-ICAP/0.5.6
	Connection: keep-alive
	ISTag: CI0001-1.1.1
```
