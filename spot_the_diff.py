import os, report, scan, sys

try:
	mode = sys.argv[1].lower()
	url = sys.argv[2].lower()
except:
	print "\n[ERROR] Please enter a mode and URL. Note: Date is optional to select which saved scan to compare against."
	print "Correct usage: ./spot_the_diff.py [diff | scan] http://www.someurl.com [OPTIONAL: YY-MM-DD] \n"
	exit()

if mode == "diff":
	try:
		date = sys.argv[3]
	except:
		date = "None"
		
	current = scan.grab(url)
	report.genReport(url, str(current), date) 

elif mode == "scan":
	report.saveScan(url, str(scan.grab(url)), False)

else:
	print "Invalid mode choice:", mode
