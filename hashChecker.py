#!/usr/bin/python3.6
#^^This is the location of python on Debian Jessie

#my MD5 checker
#started 05/03/2017
#functional 05/04/17

import sys      #for command line arguments
import os       #for file system access
import hashlib  #for MD5 hashing

#check for two command line arguments
#note that there is always one command line argument
#which is the python file itself at index[0]
if len(sys.argv)<3:
    print('Usage: myMD5Checker.py [/path/to/file] [supplied hash]')
    sys.exit()
elif len(sys.argv)>3:
    print('Usage: myMD5Checker.py [/path/to/file] [supplied hash]')
    sys.exit()
    


#DONE: define function to make md5 hash from file
def md5Checksum(file):  
    fHash=hashlib.md5(open(file, 'rb').read())
    return fHash.hexdigest()

def sha256Checksum(file):  
    fHash=hashlib.sha256(open(file, 'rb').read())
    return fHash.hexdigest()

#DONE: define function to test if hash strings equal
def stringMatcher(string1, string2):
    return string1==string2
        
#start of main body of program
#DONE: store command line argument for supplied HASH
providedHash=sys.argv[2]
#DONE: store command line argument for file path
filePath=sys.argv[1]
#print("filePath = "+filePath)

#call md5Checksum function with the filePath
fileHashMD5=md5Checksum(filePath)
#print("printing fileHash: "+fileHash)

if stringMatcher(fileHashMD5, providedHash):
    print("The MD5 hashes are a match!")
else:
    print("MD5 HASH NOT A MATCH!")
    
fileHashSHA256=sha256Checksum(filePath)
if stringMatcher(fileHashSHA256, providedHash):
    print("The SHA256 hashes are a match!")
else:
    print("SHA256 HASH NOT A MATCH!")
