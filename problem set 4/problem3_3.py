import math


# pads a bytearray b with p bytes per PKCS7 padding (bs is the block size in bytes); returns the padded bytearray
def add_bytes(b, p, bs):
    if p == 0:
        p = bs
    for i in range(0, p):
        b.append(p)
    return b


# pads a string s to a multiple of n bits using PKCS7 padding
def pkcs7_pad(s, n):    # paddingBitLength
    b_array = bytearray(str.encode(s))
    num_bytes = len(b_array)
    block_bytes = int(n / 8)
    pad_len = math.ceil(num_bytes / block_bytes) * block_bytes - num_bytes
    padded_array = add_bytes(b_array, pad_len, block_bytes)
    return padded_array


# test case 1
def test_1():
    p = pkcs7_pad("This is a Saturday", 160)
    print(p)


# test case 2
def test_2():
    p = pkcs7_pad("NO PAIN NO GAIN!", 128)
    print(p)

if __name__ == '__main__':
    test_1()
    test_2()
