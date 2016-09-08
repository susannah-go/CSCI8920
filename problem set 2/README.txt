Susannah Go
CSCI 8920
Week 2 Problem Set

1:
The file is problem2_1.py. This program includes functions for encryption and decryption using a Vernam cipher. The
test_vernam function tests both encryption and decryption using the example provided. It is assumed that the input -
whether it is plaintext or ciphertext - is valid.

2:
The file is problem2_2.py. The program expects a text file containing one hex string; the name of the text file is
given as a command line argument, e.g.:
$ python problem2_2.py w2p2.txt
Most of the operations are done in hex (I know we talked about taking it down to bytes, but I was having trouble
getting that to work). The code follows the procedure described in the assignment.

Other files in this directory are imported by problem2_1.py and/or problem2_2.py.

Additional Questions

Q: What is the encryption key?
A: 'ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICE'

Q: How long is it?
A: 45 characters

Q: Is it really as long as your algorithm determined?
A: No

Q: If not, then what is the actual key and it's length?
A: The actual key is 'ICE', length is 3 characters

Q: Why do you think there is a difference?
A: There is more repetition when looking at large chunks of text than small ones (i.e. the average hamming distance
between consecutive large chunks is less than the average distance between consecutive small chunks). To understand
why this occurs, note that the plaintext has many blocks of text that repeat, but they are not consecutive. To capture
this repetition, the key must be long enough to span repeating blocks of text.

As a smaller example, consider the text 'abczzzdefzzz' and suppose that it was encrypted with a key of length three.
Even though the chunk 'zzz' repeats, this fact will never be exploited with a key of length three since we only look at
the similarity between adjacent chunks. We would have to use a key of length 6 or longer to see the repetition.
