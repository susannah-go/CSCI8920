from Crypto.Util import number
from problem12_1 import modular_inverse
from problem12_1 import my_RSA
from problem12_1 import int2string
from problem12_1 import string2int
import hashlib

# RSA server that will only decrypt the same message once
class rsa_server:

    rsa = my_RSA()
    db = []  # database of hash messages

    def decrypt(self, c):

        h = hashlib.sha256()
        h.update(bytes(str(c), 'latin1'))
        my_hash = h.hexdigest()

        if my_hash in self.db:
            return "Message rejected"
        else:
            self.db.append(my_hash)
            return self.rsa.decrypt(c)

    def encrypt(self, m):
        return self.rsa.encrypt(m)

    def print_db(self):
        for i in self.db:
            print(i, end=" ")
        print()

    # since n is part of the public key I assume this is kosher
    def get_n(self):
        return self.rsa.get_n()

if __name__ == '__main__':

    s = rsa_server()
    s_n = s.get_n()
    s_e = 2 ** 16 + 1

    # demonstrate that server will only encrypt the same message once
    m = "Once upon a midnight dreary"
    print("Plaintext: " + m + "...")
    c = s.encrypt(m)
    m1 = s.decrypt(c)
    print("First attempt at decryption: " + m1)
    m2 = s.decrypt(c)
    print("Second attempt at decryption: " + m2)
    print()

    # do the attack by getting c_mask to decrypt to m
    r = number.getPrime(10)
    c_mask = c * pow(r, s_e) % s_n
    m_mask = string2int(s.decrypt(c_mask))
    m_unmask = int2string(m_mask * modular_inverse(r, s_n) % s_n)
    print("Result of decrypting masked ciphertext: " + m_unmask)
