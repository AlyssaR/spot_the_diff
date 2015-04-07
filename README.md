-----------------
| spot the diff |
-----------------

<strong>About:</strong>
An engine intended to be able to: 
  - Spider, scrape, and save a given URL as a "known good"
  - Spider, scrape, and diff (on a schedule if desired) the same URL checking for changes and malicious insertions
  - Output a user friendly report of any changes made

<strong>In the Future:</strong>
  - Expand scanner with Yara signatures
  - Change verbosity of report outputted
  - Change file format of output

<strong>Basic Usage:</strong>
./spot_the_diff.py [diff | scan] http://www.someurl.com [OPTIONAL: YY-MM-DD]
  - Date is required for doing a diff. spot_the_diff will compare the URL with the saved scan from that date if one exists

<strong>Requirements:</strong>
For spot_the_diff to work the following must be installed:
  - Python 2.7
  - Beautiful Soup
  - LXML
