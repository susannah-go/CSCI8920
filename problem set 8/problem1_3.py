import binascii
import math


# repeats a string k to make a string of length l
def repeat_key(k, l):
    new_string = k * math.ceil(l / len(k))
    offset = l - len(str(new_string))
    if offset < 0:
        new_string = new_string[:offset]
    return new_string


# given a hex string, return the highest frequency character
def get_high_char(s):
    char_freqs = {}
    highest_char = ""
    for i in range(0, int(len(s)/2)):
        j = i * 2
        hex_char = s[j:j + 2]
        if hex_char in char_freqs:  # update existing entry
            char_freqs[hex_char] += 1
            if char_freqs[hex_char] > char_freqs[highest_char]:
                highest_char = hex_char
        else:                       # add new entry
            if len(char_freqs) == 0:
                highest_char = hex_char
            char_freqs[hex_char] = 1

    return highest_char


# given a hex string, return a likely plaintext key based on the assumption that
# space ("20" in hex) is the most common character in the plaintext
def get_hex_key(s):
    return hex(int(get_high_char(s), 16) ^ int("20", 16))[2:]


# given a hex string, return a likely binary key
def get_bin_key(s):
    return bin(int(get_hex_key(s), 16))[2:].rjust(8, '0')


# given a hex string, return a likely plaintext key (one character)
def get_plain_key(s):
    return binascii.unhexlify(get_hex_key(s)).decode()


# decode a string s of hex ciphertext
def decode(s):
    bin_num_1 = int(s, 16)
    bi_len = len(s) * 4
    xor_string = repeat_key(get_bin_key(s), bi_len)
    bin_num_2 = int(xor_string, 2)
    ciphertext = hex(bin_num_1 ^ bin_num_2)[2:]
    plaintext = binascii.unhexlify(ciphertext).decode()
    print("plaintext key: " + get_plain_key(s))
    print("decoded text: " + plaintext)

if __name__ == '__main__':
    hexText = "26294f2e4f222e214f263c4f2029292a3d2a2b4f2e4f292e2c3b4f3827262c274f28202a3c4f2e282e26213c" \
              "3b4f27263c4f26213c3b26212c3b3c4f272a4f382623234f3c2c3d3a3b262126352a4f263b4f2c23203c2a23" \
              "364f2e212b4f3a21232a3c3c4f3b272a4f2a39262b2a212c2a4f263c4f20392a3d38272a23222621284f272a" \
              "4f382623234f3d2a293a3c2a4f3b204f2d2a23262a392a4f263b4f26294f20214f3b272a4f203b272a3d4f27" \
              "2e212b4f272a4f263c4f2029292a3d2a2b4f3c20222a3b272621284f3827262c274f2e2929203d2b3c4f2e4f" \
              "3d2a2e3c20214f29203d4f2e2c3b2621284f26214f2e2c2c203d2b2e212c2a4f3b204f27263c4f26213c3b26" \
              "212c3b3c4f272a4f382623234f2e2c2c2a3f3b4f263b4f2a392a214f20214f3b272a4f3c232628273b2a3c3b" \
              "4f2a39262b2a212c2a4f3b272a4f203d262826214f20294f22363b273c4f263c4f2a373f232e26212a2b4f26" \
              "214f3b27263c4f382e36"    # ciphertext provided
    print(decode(hexText))
