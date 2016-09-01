Susannah Go
CSCI 8920
Week 1 Problem Set

1a:
The file is hex2Base64.py. The implementation is straightforward, and upon execution of the program the user is
prompted for a hex string from the console. The input is case-insensitive. Errors such as an odd string or a non-hex
string are handled.

1b:
The file is b64ConversionTester.py. The program expects a text file with one hex string per line; the name of the text
file is given as a command line argument, e.g.:
$ python b64ConversionTester.py test.txt
Empty lines are skipped. As with part a the input is case-insensitive and errors such as an odd string or a non-hex
string are handled. In addition if no filename is given, or the file does not exist, these errors are also handled.

2:
The file is problem1-2.py. The user is prompted to enter two hex stings. The program validates that both strings are
valid hex and have equal length.

3:
The file is problem1-3.py. I did not have time to rank the outputs by the English plaintext frequencies so found the
key via brute force. The input and key are hard-coded; upon execution the program will display the decrypted message.
