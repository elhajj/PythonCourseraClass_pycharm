import urllib
import json

#address = 'http://python-data.dr-chuck.net/comments_42.json'
address = 'http://python-data.dr-chuck.net/comments_352551.json'

# open url, get data
uh = urllib.urlopen(address)
print 'Retrieving', address
data = uh.read()
print 'Retrieved',len(data),'characters'

# parse data
info = json.loads(data)

print type(info), 'loads returns this data type'

print 'Counts:', len(info['comments'])

vals = info.values()
print type(vals), '.values returns this type'
vals = vals[1]
mylist = []

for i in vals:
    mylist.append(i['count'])

print sum(mylist)
