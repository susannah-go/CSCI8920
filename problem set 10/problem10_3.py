from problem10_2 import make_mac
from problem10_2 import custom_sha1
import os


class Server:

    # generate random secret 16-byte key
    secret_key = "NO PAIN NO GAIN!"
    # secret_key = os.urandom(16).decode('latin1')

    def create_mac(self, message):
        return make_mac(self.secret_key, message)

    def verify_mac(self, message, user_mac):
        valid_mac = make_mac(self.secret_key, message)
        return user_mac == valid_mac

if __name__ == '__main__':

    orig_message = "comment1=Crypto%20Gurus;userdata=foo;comment2=%20hereAt%20UNO%20Omaha%20NE%20USA"
    extension = ";admin=true"

    s = Server()

    # get new mac
    orig_mac = s.create_mac(orig_message)
    new_mac = custom_sha1(extension,
                          int(orig_mac[:8], 16),
                          int(orig_mac[8:16], 16),
                          int(orig_mac[16:24], 16),
                          int(orig_mac[24:32], 16),
                          int(orig_mac[32:], 16))
    # print("New mac: " + new_mac)

    # guess key_length from 1 to 20 bytes
    solved = False
    for i in range(1, 21):
        key_length = i * 8

        # create padding - all in binary
        my_bytes = ""
        for n in range(len(orig_message)):
            my_bytes+='{0:08b}'.format(ord(orig_message[n]))
        bits = my_bytes+"1"
        p_bits = bits
        #pad until guessed key length + message length equals 448 mod 512
        while (key_length + len(p_bits))%512 != 448:
            p_bits+= "0"
        #append the original length
        p_bits+= '{0:064b}'.format(len(bits) - 1)

        #  binary -> bytes
        padded_message = ""
        temp = p_bits
        while temp != "":
            i = chr(int(temp[:8], 2))
            padded_message += i
            temp = temp[8:]

        # print("New message: " + str(bytes(padded_message + extension, 'latin1')))
        solved = s.verify_mac(padded_message + extension, new_mac)

        if solved:
            print(solved)
            break

    if not solved:
        print("Forgery failed. :(")
