import binascii
import math


# ciphertext provided
hexText = "26294f2e4f222e214f263c4f2029292a3d2a2b4f2e4f292e2c3b4f3827262c274f28202a3c4f2e282e26213c" \
             "3b4f27263c4f26213c3b26212c3b3c4f272a4f382623234f3c2c3d3a3b262126352a4f263b4f2c23203c2a23" \
             "364f2e212b4f3a21232a3c3c4f3b272a4f2a39262b2a212c2a4f263c4f20392a3d38272a23222621284f272a" \
             "4f382623234f3d2a293a3c2a4f3b204f2d2a23262a392a4f263b4f26294f20214f3b272a4f203b272a3d4f27" \
             "2e212b4f272a4f263c4f2029292a3d2a2b4f3c20222a3b272621284f3827262c274f2e2929203d2b3c4f2e4f" \
             "3d2a2e3c20214f29203d4f2e2c3b2621284f26214f2e2c2c203d2b2e212c2a4f3b204f27263c4f26213c3b26" \
             "212c3b3c4f272a4f382623234f2e2c2c2a3f3b4f263b4f2a392a214f20214f3b272a4f3c232628273b2a3c3b" \
             "4f2a39262b2a212c2a4f3b272a4f203d262826214f20294f22363b273c4f263c4f2a373f232e26212a2b4f26" \
             "214f3b27263c4f382e36"

# key found by inspection
hexKey = '4f'

# convert key to binary
binKey = bin(int(hexKey, 16))[2:]
binKey = binKey.rjust(8, '0')

# repeat binary key as needed to match length of hexText
biLen = len(hexText) * 4
xorString = (binKey * math.ceil((biLen / 8)))
offset = biLen - len(xorString)
if offset < 0:
    xorString = xorString[:offset]

# decode
binNum1 = int(hexText, 16)
binNum2 = int(xorString, 2)
ciphertext = hex(binNum1 ^ binNum2)[2:]
plaintext = binascii.unhexlify(ciphertext).decode()
print("decoded text: " + plaintext)
