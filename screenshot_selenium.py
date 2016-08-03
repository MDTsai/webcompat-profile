#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def screenshot_url_chrome(url):
	from time import sleep

	# Get instance of Chrome WebDriver, replace webdriver path you download
	print "Open new chrome window"
	chrome = webdriver.Chrome("/usr/local/selenium/webdriver/chromedriver/chromedriver")

	sleep(5)
	
	# Navigate to given URL until load done
	print "Opening Site http://" + url
	chrome.get("http://" + url)

	# Resize window, screenshot of web page is 810x600
	# all visible region (double in retina screen)
	print "Resize window size"
	chrome.set_window_size(810, 671)

	print "Captured screenshot"
	chrome.save_screenshot("chrometest/" + url + ".jpg")

	chrome_url = chrome.current_url

	print "Close chrome window"
	chrome.quit()

	return chrome_url

def screenshot_url_firefox(url):
	from time import sleep

	# Get instance of Firefox WebDriver
	print "Open new Firefox window"
	firefox = webdriver.Firefox()

	sleep(5)
	
	# Navigate to given URL until load done
	print "Opening Site http://" + url
	firefox.get("http://" + url)

	# Resize window, screenshot of web page (actual size)
	# need to crop to 810x600 (sometimes smaller)
	print "Resize window size"
	firefox.set_window_size(800, 608)

	print "Captured screenshot"
	firefox.save_screenshot("firefoxtest/" + url + ".jpg")

	firefox_url = firefox.current_url

	print "Close Firefox window"
	firefox.quit()

	return firefox_url

if __name__ == "__main__":
	import traceback
	import logging
	import sys

	if len(sys.argv) < 3:
		print "Usage: python screenshot_selenium.py source.txt result.txt"
		sys.exit()

	list = open(sys.argv[1])
	output = open(sys.argv[2], "w")

	for domain in list:
		# to prevent load empty line
		if len(domain) > 2:
			try:
				chrome_url = screenshot_url_chrome(domain[:-1])
				firefox_url = screenshot_url_firefox(domain[:-1])
				# output format: URL chrome_redirected_URL firefox_redirected_URL
				output.write(domain[:-1] + " " + chrome_url + " " + firefox_url + "\n")
				output.flush()
			except Exception as e:
				print domain[:-1] + " error"
				output.write(domain + " error \n")

	list.close()
	output.close()
