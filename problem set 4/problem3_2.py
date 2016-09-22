import binascii
import sys


# takes in a hex string s, returns true if a repeated block of size 16 bytes (32 hex characters) is found, otherwise
# returns false. This code borrowed from
# http://stackoverflow.com/questions/25925462/finding-the-largest-repeating-substring
def repeated_block(s):
    blocks = []
    found = False
    for i in range(0, len(s) - 32):
            substring = s[i:i + 32]
            blocks.append(substring)
    for b in blocks:
        if blocks.count(b) > 1:
            found = True
            break
    return found

if __name__ == '__main__':
    # exit if no filename is provided
    if len(sys.argv) < 2:
        sys.exit("Error: no filename provided")

    # process every line in the input file
    try:
        with open(sys.argv[1]) as f:
            line_num = 1
            for x in f:
                hex_string = str(binascii.hexlify(binascii.a2b_base64(x)))[2:-1]    # convert base 64 to hex
                if repeated_block(hex_string):
                    print("Line " + str(line_num) + " was encrypted AES ECB.")
                line_num += 1
    except IOError as e:
        sys.exit("Error: invalid filename")
