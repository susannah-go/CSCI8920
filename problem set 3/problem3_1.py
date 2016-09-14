from Crypto.Cipher import AES
import base64
import sys

try:
    with open(sys.argv[1]) as f:

        # AES-KEYToChange
        key = b'NO PAIN NO GAIN!'

        # base64 -> bytes
        ciphertext = base64.b64decode(f.read())

        # decrypt message to bytes
        cipher = AES.new(key, AES.MODE_ECB)
        plaintext = cipher.decrypt(ciphertext)

        # bytes -> string
        print("Decrypted plaintext:\n\n" + plaintext.decode())

except IOError as e:
    sys.exit("Error: invalid filename")
