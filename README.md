### **PhotoMeta** ###

A quick and dirty script to read the metadata in photos, get the creation date and time (if available) and then move the photo to the appropriate folder.  (Normally in the format of Pictures/Year/Month)

Requires:

* Python 2

* exifread <https://github.com/ianare/exif-py>

From the command line, "photometa.py fromdir todir"

* "fromdir" is the directory to read the photos from

* "todir" is the base directory to copy the photos in to