import urllib2
import simplejson
import unicodecsv

req = urllib2.Request("https://2014.foss4g.org/map-gallery/map-gallery-feed")
opener = urllib2.build_opener()
f = opener.open(req)
j = simplejson.load(f)

titles = []
for rec in j:
    titles.append([rec['title']])
print titles

with open('titles.csv', 'wb') as f:
    writer = unicodecsv.writer(f)
    writer.writerows(titles)