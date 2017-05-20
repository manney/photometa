#! /usr/bin/python
# -*- coding: utf-8 -*-

import exifread
import sys
import os
import datetime
import shutil


def getdir(directory):
    listdir = os.listdir(directory)
    dic = {}
    for x in listdir:
        f = open(os.path.join(directory, x), 'rb')
        tags = exifread.process_file(f)
        for y in tags:
            if y == 'Image DateTime':
                year = int(str(tags[y])[:4])
                month = int(str(tags[y])[5:7])
                day = int(str(tags[y])[8:10])
                dic[os.path.join(directory, x)] = datetime.date(year, month, day)
        f.close()
    return dic


def movedir(dic, todir):
    for x in dic:
        year = dic[x].strftime('%Y')
        month = dic[x].strftime('%B')
        newdir = os.path.join(todir, year, month)
        if not os.path.exists(newdir):
            print "Creating " + newdir
            os.makedirs(newdir)
        newfn = os.path.join(newdir, os.path.basename(x))
        print 'Copying: ' + newfn
        if not os.path.exists(newfn):
            shutil.copy2(x, newfn)
        else:
            print '-- ERROR: Already exists!'


def main(fromdir, todir):
    dic = getdir(fromdir)
    print str(len(dic)) + ' images in "' + fromdir + '"'
    movedir(dic, todir)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
