import urllib2
import simplejson
import unicodecsv

req = urllib2.Request("https://2014.foss4g.org/map-gallery/map-gallery-feed")
opener = urllib2.build_opener()
f = opener.open(req)
j = simplejson.load(f)

maps = [['ID','Title','Best open source software integration','Best open source data integration','Best static map (digital display)','Best web map application','Best overall cartographic display','Best anti-map map','Most unique map','Comments']]                 
for rec in j:
    soft = ""
    data = ""
    web = ""
    static = ""

    if "Open Source software integration" in rec['category']:
        soft = 'x'
    if "Open Source data integration" in rec['category']:
        data = 'x'
    if "Web Map Application" in rec['category']:
        web = 'x'
    if "Static Map" in rec['category']:
        static = 'x'
                    
    maps.append([rec['id'],rec['title'],soft,data,web,static])

for map in maps: print map

with open('mapgallery.csv', 'wb') as f:
    writer = unicodecsv.writer(f)
    writer.writerows(maps)