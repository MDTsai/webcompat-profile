This repository contains some scripts I used to grab, parse and analyze top sites.

Description:
	alexa_topdomain_crawler.sh: used to grab top 500 domains from alexa.com of specific country.
		Usage: ./alexa_topdomain_crawler.sh $COUNTRY_CODE, like CN. Outputs are in current folder named as $COUNTRY_CODE. each alexa_$INDEX.html contains 25 domains.

	alexa_topdomain_parser.py: used to parse top domains from alexa_topdomain_crawler.sh.
		Usage: python alexa_topdomain_parser.py result.txt. result.txt contains domain name in each line.

	screehshot_selenium.py: used to grab site screenshot of chrome and firefox by selenium webdriver.
		Usage: python screenshot_selenium.py source.txt result.txt, source.txt contains site address without protocol in each line. result.txt contains site name, redirected URL of chrome and firefox.