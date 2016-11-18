from Crypto.Util import number
import binascii


# returns t such that at = 1 mod n if a is invertible
# code adapted from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def modular_inverse(a, n):
    t = 0
    new_t = 1

    r = n
    new_r = a

    while new_r != 0:
        q = r // new_r

        temp_t = t - q * new_t
        t = new_t
        new_t = temp_t

        temp_r = r - q * new_r
        r = new_r
        new_r = temp_r

    if r > 1:
        return -1    # a is not invertible

    if t < 0:
        t += n

    return t


def string2int(s):
    s = bytes(s, 'latin1')
    s = str(binascii.hexlify(s))
    s = s[2:-1]
    s = bin(int(s, 16))[2:]
    s = int(s, 2)
    return s


def int2string(i):
    i = bin(i)[2:]
    ret_string = ""
    while len(i) % 8 != 0:  # add leading zeros
        i = "0" + i
    for j in range(len(i) // 8):
        block = i[8 * j: 8 * j + 8]
        ret_string += chr(int(block, 2))
    return ret_string


class my_RSA:

    d = -1
    while d < 0:
        p = number.getPrime(512)
        q = number.getPrime(512)
        n = p * q
        et = (p - 1) * (q - 1)
        e = 2 ** 16 + 1
        d = modular_inverse(e, et)

    def encrypt(self, my_m):
        my_m = string2int(my_m)
        return pow(my_m, self.e, self.n)

    def decrypt(self, my_c):
        my_c = pow(my_c, self.d, self.n)
        return int2string(my_c)

    def get_n(self):
        return self.n


if __name__ == '__main__':

    m = "Just keep swimming, just keep swimming."
    print("Plaintext: " + m)

    rsa = my_RSA()

    c = rsa.encrypt(m)
    print("Ciphertext: " + str(c))

    p = rsa.decrypt(c)
    print("Decoded ciphertext: " + p)
