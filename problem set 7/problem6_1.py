from problem3_1 import encrypt_ecb
from problem3_2 import detect_ecb
from problem6_2 import valid_padding
import base64
import binascii
import os


class Server:

    # generate random AES key
    random_unknown_key = os.urandom(16)

    # generate 10-20 random bytes
    num_bytes = 10 + os.urandom(1)[0] % 11
    foo = os.urandom(num_bytes)
    random_bytes = str(foo, 'latin1')

    def aes_128_ecb(self, attacker_encrypted_data):

        with open("w5p1.txt") as f:     # takes about 3.5 seconds
        # with open("Cookie64.txt") as f: # takes about 2.3 seconds
            unknown_string = str(base64.b64decode(f.read()), 'latin1')

        return encrypt_ecb(bytes(
            self.random_bytes + attacker_encrypted_data + unknown_string, 'latin1'), self.random_unknown_key, True)


# returns the block sized used by the server (should return 16 since the server encrypts with AES)
def find_block_size(server):

    start_size = len(server.aes_128_ecb(""))       # output size for dummy string of length 0
    output_length_1 = 0                            # output size for jump 1

    jump_1 = 0  # first jump in output size
    jump_2 = 0  # second jump in output size

    # try input strings of different lengths
    dummy_length = 1
    while jump_2 == 0:
        dummy_string = "x" * dummy_length
        cur_output_length = len(server.aes_128_ecb(dummy_string))

        if jump_1 == 0 and cur_output_length > start_size:
            jump_1 = dummy_length
            output_length_1 = cur_output_length

        if jump_1 > 0:
            if cur_output_length > output_length_1:
                jump_2 = dummy_length
                break

        dummy_length += 1

    return jump_2 - jump_1


# decode byte with offset o, bytearray b, server server, and block size b_size
# return decoded byte
def decode_byte(o, b1, server, b_size):

    decoded_byte = 0

    for k in range(0, 256):
        b1[o + b_size - 1] = k
        c_text = server.aes_128_ecb(str(bytes(b1), 'latin1'))
        if detect_ecb(binascii.hexlify(c_text)):
            decoded_byte = k
            break

    return decoded_byte


# make offset block to get first n bytes at end of a block
def make_offset_block(n, blocksize):
    return [ord('x')] * (blocksize - 1 - n)


if __name__ == '__main__':

    s = Server()

    # find the block size used by the server
    block_size = find_block_size(s)

    # try to detect ecb mode and the offset for the prefix length
    ecb_detected = False
    offset = 0
    for i in range(0, block_size):
        two_blocks = [ord('x')] * (block_size * 2 + i)
        ecb_detected = detect_ecb(binascii.hexlify(s.aes_128_ecb(str(bytes(two_blocks), 'latin1'))))
        if ecb_detected:
            offset = i
            break

    # decrypt the unknown string
    if ecb_detected:
        dummy_block = [ord('x')] * offset
        match_block = [ord('x')] * block_size   # block used to match unknown bytes
        plain_blocks = []

        i = 0
        while True:

            # controls offset so the next unknown byte is always the last in a block
            offset_block = make_offset_block(i % block_size, block_size)

            b = dummy_block + match_block + offset_block

            p_byte = decode_byte(offset, b, s, block_size)
            if p_byte == 0:
                break

            plain_blocks.append(chr(p_byte))

            # update decrypt_block
            match_block[len(match_block) - 1] = p_byte
            for j in range(0, len(match_block) - 1):
                match_block[j] = match_block[j + 1]

            i += 1

        plaintext = valid_padding(''.join(plain_blocks))
    else:
        print("ECB not detected.")
