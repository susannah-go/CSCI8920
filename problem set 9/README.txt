Susannah Go
CSCI 8920
Week 9 Problem Set

#1-2: The file is problem9_1_2.py. Upon execution the program 1) decrypts the ciphertext in w9enc.txt and 2) re-encrypts this data and compares it to the original ciphertext. Upon manual inspection the ciphertexts appear to be nearly identical.

#3: The file is problem9_3.py. Upon execution the program injects ";admin=true;" into the string from Assignment 7. I used a lot of the same code - the main difference between the two is that with CBC mode the bit-flipping occurred in the block BEFORE where you wanted the injected plaintext to occur, and in CTR mode it happens all in the same block.
