'''Generates small and medium gallery images from a set of large originals

Some maps will be tall, some wide, some square so we want to simply maintain the ratio and resize down to a set maximum.
'''

from wand.image import Image
from os import listdir
from os.path import isfile, join

small_size = 400
med_size = 1280

img_path = "/Users/twelch/src/foss4g2014-wordpress/uploads/mapgallery/"
large_path = img_path+"large/"
med_path = img_path+"medium/"
small_path = img_path+"small/"

#Get list of files in directory
img_files = [ f for f in listdir(large_path) if isfile(join(large_path,f)) ]

print "Looking for images in: " + img_path

print "Found the following: " + str(img_files)

for f in img_files:
    if f.startswith("."):
        print "Not an image file: " + str(f)
    else:
        print "Processing image: "+f
        #Create image objects for small and medium using original large
        mi = Image(filename=join(large_path,f))
        si = mi.clone()

        print 'Original: '+str(mi.width)+'x'+str(mi.height)

        #Resize maintaining aspect ratio
        mi.transform(resize=str(med_size)+'x'+str(med_size)+'>')
        print 'Medium: '+str(mi.width)+'x'+str(mi.height)
        si.transform(resize=str(small_size)+'x'+str(small_size)+'>')
        print 'Small: '+str(si.width)+'x'+str(si.height)

        #Convert to JPEG if necessary and save as new file
        mf = join(med_path,f)
        if mi.format != 'JPEG':
            mi.convert('jpeg')
        mi.save(filename=mf)

        sf = join(small_path,f)
        if si.format != 'JPEG':
            si.convert('jpeg')
        si.save(filename=sf)
        