from Crypto.Cipher import AES
from problem1_2 import binary_xor
from problem3_1 import decrypt_ecb
from problem3_1 import encrypt_ecb
from problem3_3 import pkcs7_pad
import base64
import binascii


key = b'NO PAIN NO GAIN!'  # AESKeyToChange
global_iv = bytes(bytearray(b'\x00' * 16))


# use built-in CBC mode with ciphertext c and key k to evaluate output
# does not do "chopping" of PKCS7 padding
def test_decrypt(c, k, iv):
    cipher = AES.new(k, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(c)
    return plaintext.decode()


# use built-in CBC mode with plaintext p and key k to evaluate output
def test_encrypt(p, k, iv):
    p = bytes(pkcs7_pad(p.decode('latin1'), 128))   # add in PKCS7 padding
    cipher = AES.new(k, AES.MODE_CBC, iv)
    c_text = cipher.encrypt(p)
    return c_text


# CBC mode implemented by hand with byte plaintext p and key k
def encrypt_cbc(p, k, iv):

    p = pkcs7_pad(p.decode('latin1'), 128)

    # make list of blocks
    blocks = []
    for i in range(0, int(len(p)/16)):
        b = p[i * 16:i * 16 + 16]
        blocks.append(b)

    # xor and encrypt to get ciphertext
    h1 = binascii.hexlify(iv)
    c_text = []
    for b in blocks:
        h2 = binascii.hexlify(b)
        x = binary_xor(h1.decode('latin1'), h2.decode('latin1'))
        x = hex(int(x, 2))[2:].zfill(32)
        do_aes = encrypt_ecb(binascii.unhexlify(x), k, False)
        h1 = binascii.hexlify(do_aes)  # update h1 for next iteration
        c_text.append(str(do_aes, 'latin1'))

    return ''.join(c_text)


# encodes a plaintext string to bytes
def my_encode(s):
    b = []
    for c in s:
        b.append(ord(c))
    return bytes(b)


# chop off any PKCS7 padding bytes from string p and return string
def chop(p):
    b_array = bytearray(str.encode(p))
    last_byte = b_array[-1]

    if last_byte <= 16:

        valid_padding = True
        for k in range(1, last_byte + 1):
            if b_array[0 - k] != last_byte:
                valid_padding = False
                break

        if valid_padding:
            for k in range(0, last_byte):
                b_array.pop()

    return bytes(b_array).decode('latin1')


# CBC mode implemented by hand with ciphertext c and key k
def decrypt_cbc(c, k, iv):

    # make list of blocks
    blocks = []
    for i in range(0, int(len(c)/16)):
        b = c[i * 16:i * 16 + 16]
        blocks.append(b)

    # decrypt and xor to get plaintext
    h1 = binascii.hexlify(iv)
    plain_blocks = []
    for b in blocks:
        undo_aes = my_encode(decrypt_ecb(b, k))
        h2 = binascii.hexlify(undo_aes)
        x = binary_xor(h1.decode('latin1'), h2.decode('latin1'))
        h1 = binascii.hexlify(b)  # update h1 for next iteration
        x = hex(int(x, 2))[2:].zfill(32)
        plain_block = str(binascii.unhexlify(x), 'latin1')
        plain_blocks.append(plain_block)

    plaintext = ''.join(plain_blocks)

    return chop(plaintext)

if __name__ == '__main__':
    with open("w4p1.txt") as f:

        # decode base64 -> bytes
        ciphertext = base64.b64decode(f.read())

        # use built-in decryption CBC mode
        # print(test_decrypt(ciphertext, key, global_iv))

        # use decryption CBC mode implemented by hand
        print(decrypt_cbc(ciphertext, key, global_iv))

        # use built-in encryption CBC mode
        # print(test_encrypt(b'So close, no mat', key, global_iv))
        # print(base64.b64encode(test_encrypt(b'hello darkness my old friend', key, global_iv)))

        # use encryption CBC mode implemented by hand
        # print(encrypt_cbc(b'So close, no mat', key, global_iv))
        # print(base64.b64encode(bytes(encrypt_cbc(b'hello darkness my old friend', key, global_iv), 'latin1')))
