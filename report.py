from bs4 import BeautifulSoup
import analyze, os, re, time

def genReport(url, new_scan, date):
	print "[+] Generating report..."

	### In future do this for each page in list and save to new list
	changes = analyzePage(url, new_scan, date)
	filepath = getFilePath(url, False).split("/")

	report = "<html><head><title>Summary of Changes for " + filepath[2] + "</title></head>\n"
	report = report + changes + "</body></html>"
	
	#Write changes to compiled report
	filename = "./reports/" + "/".join(filepath[2:4]) + "/report.html"
	output = open(filename, "w+")
	output.write(report)
	print "[+] Saved final report in: " + filename
	output.close()

def getFilePath(url, isReport):
	#Extract important parts of URL
	test = re.compile("(^https?\://){0,1}(www\.)?(?P<domain>[^\/]+\.\w{3})/?(?P<page>.*)")
	domain = test.search(url).group('domain')
	siteStruct = test.search(url).group('page').split("/")

	page = siteStruct[-1] #Last element is actual page
	siteStruct = siteStruct[:-1] #Site structure should exclude last page
	
	if isReport: #Save separately if is a report
		curFolder = "./reports/" + domain
	else: 
		curFolder = "./scans/" + domain

	#Create directory for domain
	if not os.path.exists(curFolder):
		os.makedirs(curFolder)

	#Create directory for todays scan
	curFolder = curFolder + "/" + time.strftime("%y-%m-%d")
	if not os.path.exists(curFolder):
		os.makedirs(curFolder)
	
	#Save page in domain structure
	for level in siteStruct:
		curFolder = curFolder + "/" + level
		if not os.path.exists(curFolder):
			os.makedirs(curFolder)

	#If no extension, guess that it's an HTML page
	try:
		hasExt = re.compile(".*\.[a-zA-Z]{2,4}$")
		hasExt.search(page).group(1)
	except:
		if page == "":
			page = "index"
		page = page + ".html"

	path = curFolder + "/" + page
	return path

def loadScan(url, date, isReport):
	print "[+] Loading scan..."
	filepath = getFilePath(url, isReport).split('/')
	filepath[3] = date
	filepath = "/".join(filepath)
	### domain = "/".join(filepath[:2])
	### Get highest value/most recent path
	### In future return list of soups
	return BeautifulSoup(open(filepath, 'r').read())

def analyzePage(url, new_scan, date):
	#Set up report structure
	page = getFilePath(url, False).split("/")[-1]
	report = "<html><head><title>" + page + "</title></head>\n<body>"
	diff = "<h2>SpotTheDiff: " + page + "</h2>\n"
	diff = diff + "<h3>Changes from " + date + " (-) to " + time.strftime("%y-%m-%d") + " (+)</h3><br>\n"
	
	#Add data 
	changes = str(analyze.diffy(url, new_scan, date))
	if changes == "":
		changes = "<strong>No changes.</strong>"
	diff = diff + changes 

	#Save
	report = report + diff + "</body></html>"
	saveScan(url, report, True)
	return diff

def saveScan(url, scan, isReport):
	filename = getFilePath(url, isReport)

	output = open(filename, "w+")
	output.write(scan)
	print "[+] Saved scan in: " + filename
	output.close()