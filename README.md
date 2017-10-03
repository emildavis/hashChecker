hashChecker
======
hashChecker is a command line program written in Python 3.6 used to check MD5 and SHA256 hashes for a match. It comes from me being fed up with manually verifying long hashes which is tedius and error prone. So I wrote this quick program in Python. This program takes a file as the first command line argument and performs MD5 and SHA256 checksums on that file. It compares the generated checksums with the supplied hash in the second argument. The program returns confirmation or a statement depending if the hashes match or not, then exits. Be patient, on larger files or older computers it could take a while to compute the SHA256.

## Download
* [Version 1.0](https://github.com/emildavis/hashChecker)

## Usage
```$ git clone https://github.com/emildavis/hashChecker.git
...```

## Version 
* Version 1.0

## How-to use this code
* Written in Python 3.6
* Download/Clone hashChecker.py to your local computer. Chmod +x to make the file executable.
* Open terminal
* Usage: myMD5Checker.py [/path/to/file] [supplied hash]
* Copy the hash you wish to check from it's published source to your clipboard and paste it into the command line

## Contact
#### Developer/Company
* Homepage: 
* e-mail: emil.davis@roadrunner.com

