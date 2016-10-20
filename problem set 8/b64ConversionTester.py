from codecs import encode, decode
from hex2Base64 import hex2base64
import sys


# use a library function to convert to base64
def theirs(a):
    if len(a) % 2 == 1:
        return "Error: hex string must have even length"
    if not hex2base64.is_valid_hex(a):
        return "Error: string is not valid hex"
    de = decode(a, "hex")
    en = str(encode(de, "base64"))[2:-3]
    return en


# use my implementation to convert to base64
def mine(a):
    converter = hex2base64()
    return converter.hex2base64(a)

# exit if no filename is provided
if len(sys.argv) < 2:
    sys.exit("Error: no filename provided")

# process every line in the input file
try:
    with open(sys.argv[1]) as f:
        for x in f:
            if x == '\n':               # check for empty line
                continue
            x = x.replace(" ", "")      # delete whitespace
            x = x.replace("0x", "")     # delete prefix 0x
            x = x.lower()               # convert to lower case
            x = x.replace("\n", "")     # delete newlines

            print(theirs(x) == mine(x))
except IOError as e:
    sys.exit("Error: invalid filename")
