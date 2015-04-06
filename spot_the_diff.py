import os, report, scan, sys

try:
	mode = sys.argv[1].lower()
	url = sys.argv[2].lower()
except:
	print "\n[ERROR] Please enter a mode and URL."
	print "Correct usage: ./spot_the_diff.py [diff | scan] http://www.someurl.com [OPTIONAL: YY-MM-DD] \n"
	exit()

if mode == "diff":
	try:
		date = sys.argv[3]
	except:
		print "\n[ERROR] Please enter a date in the form: YY-MM-DD."
		exit()
		
	current = scan.grab(url)
	report.genReport(url, str(current), date) 

elif mode == "scan":
	report.saveScan(url, str(scan.grab(url)), False) #Tests by scanning and saving

else:
	print "Invalid mode choice:", mode
