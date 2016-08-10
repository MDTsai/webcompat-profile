#!/usr/bin/python
import HTMLParser
import sys
from urllib import urlopen

class Parser(HTMLParser.HTMLParser): 
    def __init__(self, output): 
        self.processingSubdomain = None
        self.processingSubdomainData = None
        self.output = output
        HTMLParser.HTMLParser.__init__(self) 
    def handle_starttag(self,tag,attrs):
        if tag == 'table':
            for name,value in attrs: 
                if name == 'id' and value == 'subdomain_table': 
                    self.processingSubdomain = True
        elif tag == 'span' and self.processingSubdomain == True:
            for name,value in attrs: 
                if name == 'class' and value == 'word-wrap':
                    self.processingSubdomainData = True

    def handle_data(self,data): 
        if self.processingSubdomainData == True:
            self.output.write(data + "\n")
            self.output.flush()

    def handle_endtag(self,tag):
        if tag == 'table' and self.processingSubdomain == True:
            self.processingSubdomain = False
        elif tag == 'span' and self.processingSubdomainData == True:
            self.processingSubdomainData = False

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print "Usage: python alexa_subdomain_parser.py source.txt result.txt"
        sys.exit()

    list = open(sys.argv[1])
    output = open(sys.argv[2], "w")
    i = 0

    for domain in list:
        url = "http://www.alexa.com/siteinfo/"+domain[:-1].lower()
        html = urlopen(url).read()
        try:
            parser=Parser(output) 
            parser.feed(html) 
        except:
            print url
        i = i+1
        if i == 100:
            break

    output.close()
