from hex2Base64 import hex2bin
from hex2Base64 import is_valid_hex
import sys


# returns the xor of two hex strings; result is in binary, leading zeros are not truncated
def binary_xor(h1, h2):
    b1 = hex2bin(h1)
    b2 = hex2bin(h2)
    bin_string = ''.join('0' if i == j else '1' for i, j in zip(b1, b2))  # binary string
    bin_string = int(bin_string, 2)             # turn into a decimal literal
    bin_string = bin(bin_string)[2:]            # turn into a binary string
    bin_string = bin_string.zfill(len(b1))      # pad leading zeros

    return bin_string


def test_case():
    h1 = "00000000000000000000000000000000"
    h2 = "536f20636c6f73652c206e6f206d6174"
    return binary_xor(h1, h2)

if __name__ == '__main__':
    # get hex strings from the user
    #hexString1 = input("Enter a hex string: ")
    #hexString2 = input("Enter a hex string: ")

    # validate data
    #if len(hexString1) != len(hexString2):
    #    sys.exit("Error: strings must have equal length")
    #if not is_valid_hex(hexString1) or not is_valid_hex(hexString2):
    #    sys.exit("Error: at least one string is not valid hex")

    #print(binary_xor(hexString1, hexString2))
    print(test_case())
