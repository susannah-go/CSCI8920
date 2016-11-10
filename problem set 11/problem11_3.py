# SRP implementation has been modified at lines 91 (setting A = 0) and 104 (setting S = 0). Both of these changes are
# on the client side. The server calculates that S = 0 in line 66, so the keys match. Since the salt also matches,
# the verification is successful even with the incorrect password. Having the server abort the login process if A == 0
# would prevent this attack. This can be implemented by commenting out line 54 and uncommenting lines 50-53.


from problem4_1 import my_encode
from problem11_1 import quick_exp
import hashlib
import hmac
import os
import sys

# global variables that client and server agree on
N = int(
    "ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff",
    16)
g = 2
k = 3
global_I = "username"
P = "password"              # correct password
fake_P = "fake password"    # incorrect password, which will still result in successful login


class Server:

    # user profile
    I = global_I
    salt = None
    v = None

    A = None
    B = None
    u = None
    K = None
    b = os.urandom(1)[0]

    def store_password(self):

        self.salt = str(os.urandom(1)[0])
        s_xH = hashlib.sha256(my_encode(self.salt + P)).hexdigest()
        s_x = int(s_xH, 16)
        self.v = quick_exp(g, s_x, N)

    def set_I(self, my_I):
        if self.I != my_I:
            sys.exit("Bad username")

    def set_A(self, my_A):
        # if A == 0:
        #     sys.exit("Aborted - login unsuccessful")
        # else:
        #     self.A = my_A
        self.A = my_A

    def get_salt(self):
        return self.salt

    def get_B(self):
        self.B = k * self.v + quick_exp(g, self.b, N)
        return self.B

    def compute_u(self):
        s_uH = hashlib.sha256(bytes(str(self.A) + str(self.B), 'latin1')).hexdigest()
        self.u = int(s_uH, 16)
        return self.u

    def create_K(self):
        s_S = quick_exp(self.A * quick_exp(self.v, self.u, N), self.b, N)  # will always = 0 if A = 0
        self.K = hashlib.sha256(bytes(str(s_S), 'latin1')).hexdigest()

    # verify signature
    def verify(self, signature):
        server_sig = hmac.new(my_encode(str(self.K)), my_encode(str(self.salt)), hashlib.sha256).hexdigest()
        if server_sig == signature:
            return "OK"
        else:
            return "Not-OK"


if __name__ == '__main__':

    s = Server()

    # create account
    s.store_password()

    # login protocol
    s.set_I("username")
    a = os.urandom(1)[0]
    A = 0  # A = quick_exp(g, a, N)
    s.set_A(A)

    salt = s.get_salt()
    B = s.get_B()

    s.compute_u()

    uH = hashlib.sha256(bytes(str(A) + str(B), 'latin1')).hexdigest()
    u = int(uH, 16)

    xH = hashlib.sha256(my_encode(salt + fake_P)).hexdigest()  # give the server an invalid password
    x = int(xH, 16)
    S = 0  # S = quick_exp(B - k * quick_exp(g, x, N), a + u * x, N)
    K = hashlib.sha256(bytes(str(S), 'latin1')).hexdigest()

    s.create_K()

    # authenticate the shared key
    my_signature = hmac.new(my_encode(str(K)), my_encode(str(salt)), hashlib.sha256).hexdigest()
    print(s.verify(my_signature))
