import urllib
import xml.etree.ElementTree as ET

# address = 'http://python-data.dr-chuck.net/comments_42.xml'
address = 'http://python-data.dr-chuck.net/comments_352547.xml'

uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)


counts = tree.findall('.//count')
print 'Count:', len(counts)

mylist = []

for count in counts:
    mysum = int(count.text)
    mylist.append(mysum)

print 'Sum:', sum(mylist)