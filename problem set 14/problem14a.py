import binascii
import hashlib
import json
import random
import time


# returns a string representation of a random number with n digits
def get_random(n):
    return str(random.randint(0, pow(10, n) - 2)).zfill(n)


# takes in a string x and returns the the hex string md5 hash of x
def md5_hash(s):
    m = hashlib.md5()
    m.update(bytes(s, 'latin1'))
    return str(binascii.hexlify(m.digest()))[2:-1]


# takes in a hex string x and returns a numeric string of length l
def reduce(s, l):
    new_sp = ""
    for c in s:
        if len(new_sp) == l:
            break
        if c.isdigit():
            new_sp += c
    return new_sp


class RainbowTableMaker:

    def __init__(self, num_chains, len_chains, len_pw):
        self.num_chains = num_chains
        self.len_chains = len_chains
        self.len_pw = len_pw

    def make_table(self):

        rainbow_table = {}

        # create chains
        for i in range(self.num_chains):

            # generate random starting point sp_0
            sp_0 = get_random(self.len_pw)

            # work through the chain
            ep = sp_0
            for j in range(self.len_chains):
                hashed = md5_hash(ep)
                ep = reduce(hashed, self.len_pw)

            # write first and last values to the table
            rainbow_table[sp_0] = ep

        return rainbow_table


if __name__ == '__main__':

    start_time = time.time()

    rt = RainbowTableMaker(400, 40000, 3)

    # create and write table to file
    with open('rainbow_table.txt', 'w') as outfile:
        json.dump(rt.make_table(), outfile)

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
