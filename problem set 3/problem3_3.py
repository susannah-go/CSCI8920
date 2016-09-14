import sys


# pads a bytearray b with n bytes per PKCS7 padding; returns the padded bytearray
def add_bytes(b, n):
    if n == 0:
        n = 16
    for i in range(0, n):
        b.append(n)
    return b


# pads a string s to length n bits using PKCS7 padding
def pkcs7_pad(s, n):    #paddingBitLength
    b_array = bytearray(str.encode(s))
    num_bytes = len(b_array)

    if num_bytes > n:
        sys.exit("Error: phrase is too long")

    max_bytes = int(n / 8)
    padded_array = add_bytes(b_array, max_bytes - num_bytes)
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
