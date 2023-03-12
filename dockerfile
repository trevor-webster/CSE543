FROM ubuntu:18.04
RUN apt-get update && apt-get install -y apt-utils curl git tar gzip
RUN apt-get install telnet && apt-get install nmap -y && apt install tcpdump -y
RUN apt-get install net-tools && apt-get install iproute2 -y
RUN apt-get install python3.7 -y && apt-get install python3-pip -y && python3.7 -m pip install scapy==2.4.5
CMD [ "/bin/bash" ]