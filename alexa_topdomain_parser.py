#!/usr/bin/python
import HTMLParser
import sys

class Parser(HTMLParser.HTMLParser): 
    def __init__(self, output): 
        self.processingSite = None
        self.processingSiteList = None
        self.output = output
        HTMLParser.HTMLParser.__init__(self) 
    def handle_starttag(self,tag,attrs):
        if tag == 'li':
            for name,value in attrs: 
                if name == 'class' and value == 'site-listing': 
                    self.processingSiteList = True
        elif tag == 'a' and self.processingSiteList == True:
            for name,value in attrs: 
                if name == 'href':
                    self.processingSite = True

    def handle_data(self,data): 
        if self.processingSite == True:
            self.output.write(data + "\n")
            self.output.flush()

    def handle_endtag(self,tag):
        if tag == 'li' and self.processingSiteList == True:
            self.processingSiteList = False
        elif tag == 'a' and self.processingSite == True:
            self.processingSite = False

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print "Usage: python alexa_topdomain_parser.py result.txt"
        sys.exit()

    output = open(sys.argv[1], "w")

    for i in range(0, 20, 1):
        fd=open('alexa_' + str(i) + '.html') 
        parser=Parser(output) 
        parser.feed(fd.read()) 

    output.close()
