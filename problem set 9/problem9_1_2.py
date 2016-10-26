from problem3_1 import encrypt_ecb
from problem4_1 import my_encode
import base64
import math
import sys


class CTRCipher:

    key = b'NO PAIN NO GAIN!'
    nonce = 0

    # decrypts ciphertext c (a bytes object) and returns plaintext p (a string)
    def decrypt(self, c):

        num_blocks = math.ceil(len(c) / 16)
        p = ""

        for b in range(0, num_blocks):

            c_block = c[b * 16: b * 16 + 16]

            counter_format = self.nonce.to_bytes(8, byteorder='little') + b.to_bytes(8, byteorder='little')

            keystream = encrypt_ecb(counter_format, self.key, False)

            for (x, y) in zip(keystream, c_block):
                p += chr(x ^ y)

        return p

    # encrypts plaintext p (a bytes object) and returns ciphertext c (a string)
    def encrypt(self, p):
        return self.decrypt(p)

if __name__ == '__main__':

    cipher = CTRCipher()
    ciphertext = None

    try:
        with open("w9enc.txt") as f:

            # decrypt w9enc.txt
            ciphertext = f.read()
            plaintext = cipher.decrypt(base64.b64decode(ciphertext))
            print(plaintext)

            # check correctness of encrypt function
            my_ciphertext = cipher.encrypt(my_encode(plaintext))
            my_ciphertext = base64.b64encode(my_encode(my_ciphertext))
            print('{0:20}: {1}'.format("Original ciphertext", str(my_encode(ciphertext))))
            print('{0:20}: {1}'.format("My ciphertext", str(my_ciphertext)))

    except IOError as e:
        sys.exit("Error: invalid filename")
