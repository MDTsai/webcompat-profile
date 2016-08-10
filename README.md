Here is how I profile top sites in specific country(region) using scripts.

###Grab and parse top domains from alexa.com of specif country

`bash alexa_topdomain_crawler.sh $COUNTRY_CODE`

Outputs are in current folder named as $COUNTRY_CODE. each alexa_$INDEX.html contains 25 domains.

`python alexa_topdomain_parser.py result.txt`

result.txt contains domain name in each line. Put this script with alexa_$INDEX.html.

###Parse subdomains

`python alexa_subdomain_parser.py source.txt result.txt`
`python alexacn_subdomain_parser.py source.txt result.txt`

source.txt contains top domain without protocol in each line. result.txt contains subdomain in each line. First script can get at most 5 subdomains from alexa.com, the second one can get at most 10 subdomains from alexa.cn, for China only.

###Grab site screenshot

`python screenshot_selenium.py source.txt result.txt`

source.txt contains site address without protocol in each line. result.txt contains site name, redirected URL of chrome and firefox. 

Only tested on Mac. Chrome only takes screenshot of visible area, on my retina screen, the screenshot resolution is double. Firefox takes screenshot of all page content. So you need to resize screenshot from Chrome (if necessary) and crop screenshot from Firefox for further comparison.

###Compare screenshot

`python similarity_comparison.py source.txt result.txt`

The algorithm treats two images as vector, dot two vector can get similarity. If it's 1 means this two images are the same. source.txt contains site address without protocol in each line. result.txt contains similarity from 0 to 1. You need to put screenshot from screenshot_selenium in chrometest and firefoxtest with this script.
