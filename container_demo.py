#!/usr/bin/python

import sys
import os

# traditional "Hello, Hello!" speach.
print ("Hello, Hello!")

# check for environment variable and print it
#   maybe set environment varialbe then demonstrate it only chaning in 
#   container

print( "SING_DEMO environment varialbe is set to: %s" % os.getenv('SING_DEMO'))

# read stdin
if not sys.stdin.isatty():
    print("begin STDIN")
    for line in sys.stdin:
        print(line.rstrip("\n\r"))
    print("end STDIN")
else:
    print("no STDIN")

# open a file?

try:
    filename = sys.argv[1]
except:
    filename = "/etc/issue"

print("Reading from file: "+filename) 

try:
    file = open(filename)
    for fline in file:
        print (fline.rstrip("\n\r"))
except:
    print("can't open file: "+filename)
