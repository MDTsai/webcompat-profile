#!/usr/bin/python
from urllib import urlopen
import requests
import time
import sys

if len(sys.argv) < 3:
    print "Usage: python alexacn_subdomain_parser.py source.txt result.txt"
    sys.exit()

list = open(sys.argv[1])
output = open(sys.argv[2], "w")

for domain in list:
    print "Get session keys of " + domain
    url = "http://www.alexa.cn/index.php?url="+domain
    html = urlopen(url).read()
    begin = html.find('showHint', 0)
    end = html.find("'", begin+10) # showHint('url,sig,keyt')
    params = html[begin+10:end].split(',') # get parameters of current session

    print "Get data of " + domain
    api = "http://www.alexa.cn/api_150710.php"
    headers = {"Content-Type" : "application/x-www-form-urlencoded"}
    payload = {'url': params[0], 'sig': params[1], 'keyt': params[2]}
    response = requests.post(api, headers = headers, data = payload)

    res_array = response.text.split('*')
    if len(res_array) != 17:
        continue # correct response should contains some statistic and subdomain result, not match then we skip this domain

    subdomains = res_array[16].split('__')
    i = 0
    for subdomain in subdomains:
        if len(subdomain) > 0:
            subdomain_array = subdomain.split(":")
            if not subdomain_array[0].endswith('OTHER'): # OTHER is useless, skip
                if subdomain_array[0].lower().endswith(domain[:-1].lower()):
                    output.write(subdomain_array[0] + "\n")
                else:
                    sub = subdomain_array[0].split('.')[0]
                    output.write(sub + '.' + domain[:-1] + "\n")
            i += 1
            if i == 11:
                break
        output.flush()

    time.sleep(100)

list.close()
output.close()