import difflib, re, report

def diffy(url, new_scan, date):
	print "[+] Looking for differences..."

	date, old_scan = report.loadScan(url, date, False)

	old_scan = re.sub(r"<br>|<br/>|<br />|<p>", "\n", str(old_scan)).splitlines()
	new_scan = re.sub(r"<br>|<br/>|<br />|<p>", "\n", str(new_scan)).splitlines()
	diff = difflib.unified_diff(old_scan, new_scan, lineterm='', n=0)

	return date, list(diff)[2:]
	
def findEvil(new_scan):
	print "All good here! That or I haven't written this method yet."