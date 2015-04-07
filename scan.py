from bs4 import BeautifulSoup
import re, urllib2

def grab(url):
	url = validify(url)
	print "[+] Grabbing", url
	
	try:
		page = urllib2.urlopen(url)
		soup = BeautifulSoup(page.read(), "lxml")
		page.close()
	except:
		print "\n[ERROR] Could not open page."
		print "Please enter in URL valid form.\n"
		exit()
	
	return soup

def spider():
	print "Spiders! Ah!"
	print "Also, note to self -> Write this method."

def validify(url):
	prefix = re.compile("https?\://www\.([^\/]+)\.\w{3}")
	www = re.compile("www\.([^\/]+)\.\w{3}")

	if prefix.search(url):
		return url
	elif www.search(url):
		return "http://" + url
	else:
		return "http://www." + url