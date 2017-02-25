#!/usr/bin/python
import requests
import sched, time

s = sched.scheduler(time.time, time.sleep)

def main(sc): 
    print "Downloading Ransomware feed..."
    ioc = []
    feed_file = requests.get('https://files.deependresearch.org/feeds/ransomware/ransomware-payment-sites.txt', verify=False).content
    outfile = 'domain,notes\n'
    for line in feed_file.splitlines():
        if line.startswith('#') or '.' not in line:
            continue
        outfile += '%s,DeepEndResearch Suspected Ransomware Payment Site\n' % line
    with open('ransomware_payment_site.csv', 'a+') as fh:
        fh.write(outfile)
    s.enter(86400, 1, main, (sc,)) 
    s.run()
     
main(0)
