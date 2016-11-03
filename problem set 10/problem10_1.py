from problem4_1 import encrypt_cbc
from problem4_1 import decrypt_cbc


class BadCBC:

    key = b'NO PAIN NO GAIN!'
    bad_iv = key
    print("Actual key: " + key.decode('latin1'))

    # encrypts plaintext with CBC mode where key = IV
    def bad_encrypt(self, plaintext):
        return bytes(encrypt_cbc(plaintext, self.key, self.bad_iv), 'latin1')

    # returns true if ciphertext s decrypts to an ASCII string, otherwise returns s
    def is_ascii(self, s):
        p = decrypt_cbc(s, self.key, self.bad_iv, False)
        try:
            if all(ord(c) < 128 for c in p):
                return True
            else:
                raise NonASCIIError
        except NonASCIIError:
            return bytes(p, 'latin1')


class NonASCIIError(Exception):
    pass

if __name__ == '__main__':

    b = BadCBC()

    # encrypt URL
    plaintext_1 = b'http://www.unomaha.edu/index.php'
    ciphertext = b.bad_encrypt(plaintext_1)

    # modify message
    empty_block = bytes(bytearray(b'\x00' * 16))
    block_head = ciphertext[0:16]
    modified_ciphertext = block_head + empty_block + block_head

    # recover key
    plaintext_2 = b.is_ascii(modified_ciphertext)

    if plaintext_2 is True:
        print("Key recovery failed. :(")
    else:
        k = ""
        for (x, y) in zip(plaintext_2[:16], plaintext_2[32:]):
            k += chr(x ^ y)
        print("Recovered key: " + k)
