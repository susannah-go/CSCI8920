from hex2Base64 import Hex2Base64
import sys


# get hex strings from the user
hexString1 = input("Enter a hex string: ")
hexString2 = input("Enter a hex string: ")

# validate data
if len(hexString1) != len(hexString2):
    sys.exit("Error: strings must have equal length")
if not Hex2Base64.is_valid_hex(hexString1) or not Hex2Base64.is_valid_hex(hexString2):
    sys.exit("Error: at least one string is not valid hex")

binNum1 = int(hexString1, 16)
binNum2 = int(hexString2, 16)

print("Output: " + hex(binNum1 ^ binNum2)[2:])
