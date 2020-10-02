# C-ICAP with TLS support

## Requirements

- **OS**: Ubuntu LTS

- **libssl 1.1**

- **OpenSSL**

## Install SSL dependencies

```
sudo apt-get install libssl-dev libssl1.1 openssl
```

## Install C-ICAP from source code

Download the [c-icap source](https://sourceforge.net/projects/c-icap/files/latest/download) and change to the icap source directory, and run the commands bellow

```
tar xvf c_icap-0.5.6.tar.gz
cd c_icap-0.5.6/
./configure --prefix=/usr/local/c-icap
make
sudo make install
```

### Generate a self signed cert (for testing)

```
cd /usr/local/c-icap && mkdir cert && cd cert
openssl req -newkey rsa:2048 -nodes -keyout key.pem -x509 -days 365 -out certificate.pem
sudo chown -R c-icap:c-icap /usr/local/c-icap/cert
```

You will need to fill up certificate parameters

### ICAP configuration

Edit the c-icap.conf file using `sudo nano /usr/local/c-icap/c-icap.conf` 

```
TlsPort 1345 tls-method=TLSv1_2 cert=/usr/local/c-icap/cert/certificate.pem key=/usr/local/c-icap/cert/key.pem
```

### Start icap server

```
sudo /usr/local/c-icap/bin/c-icap -N -D -d 10
```

### Test ICAP server for TLS support

```
sudo /usr/local/c-icap/bin/c-icap-client -i localhost -p 1345 -tls -tls-no-verify -tls-method TLSv1_2
```
