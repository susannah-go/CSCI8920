from Crypto.Cipher import AES
from problem3_3 import pkcs7_pad
import base64
import sys


# decrypt ciphertext c with key k, and return plaintext
def decrypt_ecb(c, k):
    cipher = AES.new(k, AES.MODE_ECB)
    plaintext = cipher.decrypt(c)
    return str(plaintext, 'latin1')


# encrypt plaintext p with key k, and return ciphertext
def encrypt_ecb(p, k):
    p = pkcs7_pad(p.decode(), 128)
    cipher = AES.new(k, AES.MODE_ECB)
    c_text = cipher.encrypt(bytes(p))
    return c_text


if __name__ == '__main__':
    try:
        with open(sys.argv[1]) as f:

            # AES-KEYToChange
            key = b'NO PAIN NO GAIN!'

            # base64 -> bytes
            ciphertext = base64.b64decode(f.read())

            # print(decrypt_ecb(ciphertext, key))

            foo = decrypt_ecb(ciphertext, key)
            foo = bytes(foo, 'utf-8')

            print(str(encrypt_ecb(b'no pain no gain!', key), 'latin1'))
            print(base64.b64encode(encrypt_ecb(foo, key)))

    except IOError as e:
        sys.exit("Error: invalid filename")
