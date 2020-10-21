#!/bin/bash
DIR=${0%/*}'/input/'
ODIR=${0%/*}'/output/'
rm -rf ${ODIR} > /dev/null 2>&1
mkdir -p ${ODIR}

for file in "$DIR"*.png
do
    filename=result.png
    /usr/local/c-icap/bin/c-icap-client -i 192.168.189.161 -p 1300 -s gw_rebuild -f $file -o ${ODIR}/$filename -v 2>&1 | tee /var/tmp/log.txt
done
