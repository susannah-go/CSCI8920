from problem3_1 import encrypt_ecb
from problem3_2 import repeated_block
from problem4_1 import encrypt_cbc
from problem4_1 import my_encode
from problem4_1 import test_encrypt
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

    b_array = bytearray(my_encode(plaintext))

    # randomly prepend 5-10 bytes
    random_prepend = os.urandom(1)
    num_prepend_bytes = 5 + random_prepend[0] % 6   # noOfPrependBytes
    for i in range(0, num_prepend_bytes):
        b_array.append(os.urandom(1)[0])

    # randomly append 5-10 bytes
    random_append = os.urandom(1)
    num_append_bytes = 5 + random_append[0] % 6     # noOfAppendBytes
    for j in range(0, num_append_bytes):
        b_array.insert(0, os.urandom(1)[0])

    # create modified plaintext
    plaintext = bytes(b_array)

    # encrypt
    if mode == 0:
        ciphertext = encrypt_ecb(plaintext, random_key, True)
    else:
        random_iv = os.urandom(16)
        ciphertext = bytes(my_encode(encrypt_cbc(plaintext, random_key, random_iv)))
        # ciphertext = bytes(test_encrypt(plaintext, random_key, random_iv))

    # print detected mode
    if repeated_block(binascii.hexlify(ciphertext)):
        print("ECB mode detected")
    else:
        print("CBC mode detected")
