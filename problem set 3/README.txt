Susannah Go
CSCI 8920
Week 3 Problem Set

1:
The file is problem3_1.py. The program expects a text file containing one hex string; the name of the text file is
given as a command line argument, e.g.:
$ python problem3_1.py w3p1.txt
It is assumed that the input is valid base64-encoded ciphertext encrypted with AES-128 in ECB mode. To change the key
modify line 9 of the code. This program uses the PyCryptodome library.

2:
The file is problem3_2.py. The program expects a text file containing one hex string; the name of the text file is
given as a command line argument, e.g.:
$ python problem3_2.py w3p2.txt
It is assumed that the input is all valid AES ciphertext. The program will detect all lines that appear to have been
encrypted using ECB mode. For the provided text file this program took about 12 seconds to run.

3:
The file is problem3_3.py. The main padding function (pkcs7_pad) takes the bit padding length as the second argument.

The output to "This is a Saturday" padded to 160 bits is:
bytearray(b'This is a Saturday\x02\x02')
Since 160 bits = 20 bytes and "This is a Saturday" has 18 characters (and is therefore 18 bytes long), there are two
unused bytes in the block. The unused blocks are both filled with 2's (02 in hex).

The output to "NO PAIN NO GAIN!" padded to 128 bits is:
bytearray(b'NO PAIN NO GAIN!\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10')
Since 128 bits = 16 bytes and "NO PAIN NO GAIN!" has 16 characters (and is therefore 16 bytes long), there are no
unused bytes in the block. Therefore a full dummy block of 16 bytes is used with all 16's (10 in hex).
