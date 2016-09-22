from problem3_1 import encrypt_ecb
from problem3_2 import repeated_block
from problem4_1 import test_encrypt  # using built-in cbc since mine isn't working
import binascii
import os

# generate a random AES key (16 bytes)
random_key = os.urandom(16)
ciphertext = None

with open("w4p2.txt") as f:     # inputFile
    plaintext = f.read()

    # randomly choose ecb or cbc
    random_num = os.urandom(1)
    mode = random_num[0] % 2    # 0 for ECB, 1 for CBC

    # print selected mode
    if mode == 0:   # randomChoiceofECB-CBC
        print("ECB mode selected")
    else:
        print("CBC mode selected")

    # randomly prepend 5-10 bytes
    random_prepend = os.urandom(1)
    num_prepend_bytes = 5 + random_prepend[0] % 6   #noOfPrependBytes
    for i in range(0, num_prepend_bytes):
        r1 = os.urandom(1)
        # prepend bytes

    # randomly append 5-10 bytes
    random_append = os.urandom(1)
    num_append_bytes = 5 + random_append[0] % 6     #noOfAppendBytes
    for j in range(0, num_append_bytes):
        r2 = os.urandom(1)
        # append bytes

    # encrypt
    if mode == 0:
        ciphertext = encrypt_ecb(bytes(plaintext, 'latin1'), random_key)
    else:
        random_iv = os.urandom(16)
        ciphertext = bytes(test_encrypt(bytes(plaintext, 'latin1'), random_key, random_iv))

    # print detected mode
    if repeated_block(binascii.hexlify(ciphertext)):
        print("ECB mode detected")
    else:
        print("CBC mode detected")
