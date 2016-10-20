from hex2Base64 import Hex2Base64
from problem1_3 import get_plain_key
from problem2_1 import decrypt_vernam, text2bin
import binascii
import math
import sys


# count the number of 1's in a binary string s
def count_ones(s):
    ones = 0
    for c in s:
        if c == '1':
            ones += 1
    return ones


# compute the hamming distance between binary strings s1 and string s2
def get_ham(s1, s2):
    if s1 and s2:
        xor_string = bin(int(s1, 2) ^ int(s2, 2))[2:]
    elif not s1:
        xor_string = s2
    else:
        xor_string = s1

    return count_ones(xor_string)


# test get_ham function with strings provided
def test_ham():
    t1 = "is this heaven"
    t2 = "no it's iowa!!"
    print(get_ham(text2bin(t1), text2bin(t2)) == 34)


# returns the most likely key length for hex string c.
# considers key lengths 2 bytes to 45 bytes
def guess_key_length(c):
    key_lengths = {}    # dictionary of key lengths and avg normalized hamming distance
    max_key_length = min(46 * 2, int(len(c)/2))

    best_ham_dist = max_key_length * 8 * 2
    best_key_length = max_key_length

    for i in range(2, max_key_length):
        chunk_2 = ""
        ham_dist = 0
        comparisons = 0

        for j in range(0, math.ceil(len(c) / (2 * i))):
            k = j * i
            chunk_1 = chunk_2
            chunk_2 = c[k:k + (2 * i)]
            if j == 0:
                continue
            comparisons += 1

            ham_dist += get_ham(Hex2Base64.hex2bin(chunk_1), Hex2Base64.hex2bin(chunk_2))/i

        avg_ham_dist = ham_dist/comparisons
        key_lengths[i] = avg_ham_dist

        if avg_ham_dist < best_ham_dist:
            best_ham_dist = avg_ham_dist
            best_key_length = i

    return best_key_length


# return a list of chunks of length n from ciphertext c
def make_chunks(c, n):
    chunks = []
    for i in range(0, math.ceil(len(c)/n)):
        chunks.append(c[i * n:i * n + n])
    return chunks


# take in a list of chunks l and return a list of blocks containing the first character from every chunk in l, second
# character from every chunk in l, third character from every chunk in l, etc.
def make_blocks(l):
    char_blocks = []            # initialize char_blocks with empty lists
    for i in range(0, int(len(l[0])/2)):
        char_blocks.append([])

    for i in range(0, len(l)):  # populate lists with pairs of characters
        for j in range(0, int(len(l[i])/2)):
            k = j * 2
            char_blocks[j].append(l[i][k])
            char_blocks[j].append(l[i][k + 1])

    string_blocks = []          # join characters into strings
    for i in range(0, len(char_blocks)):
        string_blocks.append(''.join(char_blocks[i]))
    return string_blocks


# reads a text file w2p2.txt which is assumed to contain base64 ciphertext
def read_file():
    if len(sys.argv) < 2:
        sys.exit("Error: no filename provided")

    # process every line in the input file
    try:
        with open(sys.argv[1]) as f:
            data = f.read()
    except IOError:
        sys.exit("Error: invalid filename")

    return data


# takes a hex string of ciphertext encrypted with a Vernam cipher
# (key length is 2 to 45 bytes) and attempts to break it
def break_cipher(s):
    hex_string = str(binascii.hexlify(binascii.a2b_base64(s)))[2:-1]

    blocks = make_blocks(make_chunks(hex_string, guess_key_length(hex_string)))

    key_chars = []
    for b in blocks:
        key_chars.append(get_plain_key(b))

    key = ''.join(key_chars)

    print("key: " + key)
    print(len(key))
    print("plaintext: " + decrypt_vernam(hex_string, key))

if __name__ == '__main__':
    # test_ham()
    ciphertext = read_file()
    break_cipher(ciphertext)
