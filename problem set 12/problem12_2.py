from Crypto.Util import number
from problem12_1 import modular_inverse
from problem12_1 import string2int
from problem12_1 import int2string


class bad_RSA:

    def __init__(self):
        self.d = -1
        while self.d < 0:
            self.p = number.getPrime(128)
            self.q = number.getPrime(128)
            self.n = self.p * self.q
            self.et = (self.p - 1) * (self.q - 1)
            self.e = 3
            self.d = modular_inverse(self.e, self.et)

    def encrypt(self, my_m):
        my_m = string2int(my_m)
        return pow(my_m, self.e, self.n)

    def decrypt(self, my_c):
        my_c = pow(my_c, self.d, self.n)
        return int2string(my_c)

    def get_n(self):
        return self.n

if __name__ == '__main__':

    m = "Test"
    print("Plaintext: " + m)

    r0 = bad_RSA()
    r1 = bad_RSA()
    r2 = bad_RSA()

    n0 = r0.get_n()
    n1 = r1.get_n()
    n2 = r2.get_n()

    c0 = r0.encrypt(m) % n0
    c1 = r1.encrypt(m) % n1
    c2 = r2.encrypt(m) % n2

    ms0 = n1 * n2
    ms1 = n0 * n2
    ms2 = n0 * n1
    N012 = n0 * n1 * n2

    term1 = c0 * ms0 * modular_inverse(ms0, n0)
    term2 = c1 * ms1 * modular_inverse(ms1, n1)
    term3 = c2 * ms2 * modular_inverse(ms2, n2)

    c = (term1 + term2 + term3) % N012
    plaintext = int(round(c ** (1. / 3)))
    print("Recovered plaintext: " + int2string(plaintext))
