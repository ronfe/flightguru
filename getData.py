__author__ = 'ronfe'

import urllib2, json
from bs4 import BeautifulSoup
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36'

def getData(url):
    # Bootstrap HTTP req
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    req.add_header('User-Agent', ua)

    # Derive data
    htmlDoc = opener.open(req).read()
    soup = BeautifulSoup(htmlDoc, 'html.parser')
    originRecords = soup.find_all('tr')
    records = []
    for each in originRecords:
        records.append(each.get('id'))

    # Clean and output
    outputRec = []
    for each in records:
        if each != None:
            tempGroup = each.split('-')
            outputRec.append(tempGroup[1])

    return outputRec

def getFlight(flightQ):
    # Send API req
    templateUrl = 'http://lhr.data.fr24.com/_external/planedata_json.1.4.php?f='
    req = urllib2.Request(templateUrl + flightQ)
    opener = urllib2.build_opener()
    req.add_header('User-Agent', ua)
    flightInfo = opener.open(req).read()
    returnInfo = json.loads(flightInfo)
    return returnInfo