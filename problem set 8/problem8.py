from hex2Base64 import bin2hex
from problem1_2 import binary_xor
from problem4_1 import decrypt_cbc
from problem4_1 import encrypt_cbc
from problem4_1 import my_encode
from problem6_2 import valid_padding
import base64
import binascii
import os


class Webapp:

    # class variables
    key = os.urandom(16)    # random AES key
    iv = os.urandom(16)     # random IV

    # plaintext is a function parameter
    def encrypt(self, plaintext):
        c_text = encrypt_cbc(plaintext, self.key, self.iv)
        return c_text, self.iv

    # plaintext is randomly chosen
    def random_encrypt(self):

        # randomly choose plaintext message from lines 0-9 in w8.txt
        line_num = os.urandom(1)[0] % 10
        f = open("w8.txt")
        message = f.readlines()[line_num]

        # un-base64 and encrypt message
        message = base64.b64decode(message)
        c_text = encrypt_cbc(message, self.key, self.iv)

        return c_text, self.iv

    # returns true if the decrypted plaintext has valid padding, otherwise returns false
    def decrypt(self, my_iv, c):
        p_text = decrypt_cbc(c, self.key, my_iv, False)
        return valid_padding(p_text)


def get_hex_string(s):
    return str(binascii.hexlify(s))[2:-1]


def three_xor(a1, a2, a3):
    temp = binary_xor(a1, a2)
    return binary_xor(bin2hex(temp), a3)

if __name__ == '__main__':

    w = Webapp()

    # captured[0] is the ciphertext (string); captured[1] is the iv (bytes)
    captured = w.random_encrypt()
    ciphertext = my_encode(captured[0])     # convert to bytes
    iv = captured[1]

    answer = ""

    for block_index in range(0, len(ciphertext) // 16):

        block = ciphertext[16 * block_index: 16 * block_index + 16]

        if block_index == 0:
            prev_block = bytearray(iv)
        else:
            # TODO: fix prev_block
            prev_block = bytearray(iv)
        block_answer = ""

        for byte_index in range(1, 16):

            prev_block_byte = hex(iv[-byte_index])[2:].zfill(2)

            for i in range(0, 256):

                # guess a byte
                byte_guess = my_encode(chr(i))

                #  modify the previous block with already-solved bytes
                for j in range(0, len(block_answer)):
                    solved_byte = hex(iv[-(j + 1)])[2:].zfill(2)

                    h2 = get_hex_string(my_encode(block_answer[-(j + 1)]))
                    h3 = get_hex_string(my_encode(chr(byte_index)))
                    prev_block[-(j + 1)] = int(three_xor(solved_byte, h2, h3), 2)

                h2 = get_hex_string(byte_guess)
                h3 = get_hex_string(my_encode(chr(byte_index)))
                prev_block[-byte_index] = int(three_xor(prev_block_byte, h2, h3), 2)

                # detect the correct guess
                if block_index == 0:
                    if w.decrypt(bytes(prev_block), block):
                        block_answer = chr(i) + block_answer
                else:
                    # TODO: fix this - needs to decrypt prev_block + block
                    if w.decrypt(iv, block):
                        block_answer = chr(i) + block_answer

        answer += block_answer

    print(answer)
