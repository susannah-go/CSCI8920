# crack a hash using rainbow tables
from problem14a import md5_hash
from problem14a import reduce
import json
import time


class PasswordCracker:

    def __init__(self, rainbow_table):
        self.rainbow_table = rainbow_table

    # values must match those in problem14a.py
    num_chains = 400
    len_chains = 40000
    len_pw = 3

    # secret password
    orig_password = "1824928347"
    password = orig_password[:len_pw]

    # known hash and reduction of password
    h_password = md5_hash(password)
    r_password = reduce(h_password, len(password))

    h0 = h_password
    r0 = r_password

    # gather starting points of candidate chains
    chain_candidates = set()

    def get_chains(self):

        pw_flag = False

        for i in range(self.len_chains):
            for k, v in self.rainbow_table.items():
                if v == self.r_password and k not in self.chain_candidates:
                    self.chain_candidates.add(k)
                    pw_flag = self.get_pws(k) or pw_flag

            self.r_password = reduce(md5_hash(self.r_password), self.len_pw)

        if not pw_flag:
            print("Password could not be recovered")

    # identify password candidates
    def get_pws(self, sp):

        pw_flag = False

        # initialize prev_reduce
        prev_reduce = sp

        for i in range(self.len_chains):
            if sp == self.r0:
                print("Is " + prev_reduce + " your password?")
                pw_flag = True
            prev_reduce = sp
            sp = reduce(md5_hash(sp), self.len_pw)

        return pw_flag

    def recover_password(self):
        self.get_chains()
        if not self.chain_candidates:
            print("Password could not be recovered")
            return


if __name__ == '__main__':

    start_time = time.time()

    # load rainbow table
    with open('rainbow_table.txt') as infile:
        rt = json.load(infile)

    pc = PasswordCracker(rt)
    pc.recover_password()

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
