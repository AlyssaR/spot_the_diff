from bs4 import BeautifulSoup
import analyze, os, re, time

def genReport(url, new_scan, date):
	print "[+] Generating report..."

	report = BeautifulSoup(open("./templates/template.html", 'r').read())
	
	### In future do this for each page in list
	filepath = getFilePath(url, False).split("/")
	report.oldscan.string = date
	report.newscan.string = time.strftime("%y-%m-%d")
	report.target.string = filepath[2]
	report.targetpage.string = filepath[-1]
	
	#Add results
	diff = report.diff
	diff.string = ""
	date, changes = analyzePage(url, new_scan, date)
	diff.append(report.new_string(changes[0]))
	for line in changes[1:]:
		diff.append(report.new_tag('br'))
		diff.append(report.new_string(line))

	#Write changes to compiled report
	filename = "./reports/" + "/".join(filepath[2:4]) + "/report.html"
	open(filename, "w+").write(str(report))
	print "[+] Saved final report in: " + filename

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
		if isReport:
			page = page + ".txt"
		else:
			page = page + ".html"

	path = curFolder + "/" + page
	return path

def loadScan(url, date, isReport):
	print "[+] Loading scan..."
	filepath = getFilePath(url, isReport).split('/')
	domainDir = "/".join(filepath[:3])
	latestScan = sorted(os.listdir(domainDir))
	
	#Get most recent scan
	if date is "None" and latestScan is not None:
		date = latestScan[-1]
	elif date is "None":
		print "[ERROR] No saved scans found for", url
		exit()

	filepath[3] = date
	filepath = "/".join(filepath)

	### In future return list of soups
	return date, BeautifulSoup(open(filepath, 'r').read())

def analyzePage(url, new_scan, date):
	#Set up report structure
	page = getFilePath(url, False).split("/")[-1]

	#Add data 
	date, changes = analyze.diffy(url, new_scan, date)
	if len(changes) == 0:
		changes = "No changes."

	#Save
	saveScan(url, str(changes), True)
	return date, changes

def saveScan(url, scan, isReport):
	filename = getFilePath(url, isReport)

	output = open(filename, "w+")
	output.write(scan)
	print "[+] Saved scan in: " + filename
	output.close()