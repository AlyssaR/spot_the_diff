import difflib, re, report

def diffy(url, new_scan, date):
	print "[+] Looking for differences..."

	old_scan = re.sub(r"<br>|<br/>|<br />|<p>", "\n", str(report.loadScan(url, date, False))).splitlines()
	new_scan = re.sub(r"<br>|<br/>|<br />|<p>", "\n", str(new_scan)).splitlines()
	diff = difflib.unified_diff(old_scan, new_scan, lineterm='', n=0)

	return list(diff)[2:]
	
def findEvil(new_scan):
	print "All good here! That or I haven't written this method yet."