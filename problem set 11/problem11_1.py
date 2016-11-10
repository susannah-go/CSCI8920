import hashlib
import os


# returns a shared diffie_hellman key for a given prime my_p and generator my_g
# or -1 if the algorithm fails
def diffie_hellman(my_p, my_g):

    p = my_p
    g = my_g

    # randomly generated private keys
    a = os.urandom(1)[0] % p
    b = os.urandom(1)[0] % p

    A = quick_exp(g, a, p)
    B = quick_exp(g, b, p)

    # shared keys
    s_1 = quick_exp(A, b, p)
    s_2 = quick_exp(B, a, p)

    if s_1 != s_2:
        return -1
    else:
        m = hashlib.sha256()
        m.update(bytes(str(s_1), 'latin1'))
        return m.hexdigest()


# quickly calculate a^b % p for ints a, b, p
def quick_exp(a, b, p):

    # express b as a binary string
    bin_b = str(bin(b))[2:]

    # my_list[i] is a^(2^i) % p
    my_list = []

    # populate my_list
    prev_value = a
    my_list.append(prev_value)

    for i in range(len(bin_b) - 1):
        new_value = prev_value ** 2 % p
        my_list.insert(0, new_value)
        prev_value = new_value

    # calculate and return a^b % p
    ret_value = 1

    for i in range(len(bin_b)):
        if bin_b[i] == "1":
            ret_value *= my_list[i]

    return ret_value % p

if __name__ == '__main__':

    little_p = 101
    little_g = 53

    print("Shared key for p = {}, g = {}: {}\n".format(little_p, little_g, diffie_hellman(little_p, little_g)))

    nist_prime = int("ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
    nist_g = 2

    print("Shared key for p = {}, g = {}: {}\n".format("NIST prime", nist_g, diffie_hellman(little_p, little_g)))
