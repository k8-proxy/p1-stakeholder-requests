# Icap with TLS

## Install lib ssl

```
apt-get install libssl-dev
```

## Setup ICAP
Download the icap source and change to the icap source directory, and run the commands bellow

```
./configure --prefix=/usr/local/c-icap
make
make install
```

## Setup a self signed cert (for testing)

```
cd /usr/local/c-icap && mkdir cert && cd cert
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
```


## Edit icap configuration and add the line below to enable tls
```
TlsPort 1345 tls-method=TLSv1_2 cert=/usr/local/c-icap/cert/certificate.pem key=/usr/local/c-icap/cert/key.pem
```

## Start icap server
```
/usr/local/c-icap/bin/c-icap -N -D -d 10
```

## Test icap server for tls support
```
/usr/local/c-icap/bin/c-icap-client -i localhost -p 1345 -tls -tls-no-verify -tls-method TLSv1_2
```

