from hex2Base64 import bin2hex
from problem1_2 import binary_xor
from problem4_1 import my_encode
from problem9_1_2 import CTRCipher
import binascii

my_cipher = CTRCipher()


# takes an arbitrary plaintext input string and returns a sanitized encrypted string
def sanitizer(p):

    # concatenate input string with prepend and append strings
    prepend = "comment1=raining%20MCs;userdata="
    append = ";comment2=%20like%20a%20sunny%20day%20tomorrow"
    s = prepend + p + append

    # quote out ";" and "=" characters
    s = s.replace(";", "")
    s = s.replace("=", "")
    print("Sanitized plaintext: " + s)

    # return encrypted string
    return my_cipher.encrypt(my_encode(s))


# returns true if the decrypted input string m contains ";admin=true;", otherwise returns false
def checker(m):

    # decrypt the input string
    p = my_cipher.decrypt(my_encode(m))

    print("Altered plaintext: " + p)

    test_string = ";admin=true;"
    return test_string in p


# returns the byte that the original byte of ciphertext should be replaced by so it decrypts to the new byte
def get_replacement_byte(orig, new):

    h1 = str(binascii.hexlify(my_encode(orig)))[2:-1]
    h2 = str(binascii.hexlify(my_encode("x")))[2:-1]
    h3 = str(binascii.hexlify(my_encode(new)))[2:-1]

    temp = binary_xor(h1, h2)
    r_byte = binary_xor(bin2hex(temp), h3)

    return r_byte


# inject malicious chars, bwahahaha
def injector(c):

    # byte array of ciphertext
    b_array = bytearray(my_encode(c))

    # start flipping at the 32nd byte (the first byte of a full attacker-controlled block)
    starting_byte = 32

    # plaintext we want to inject
    malicious_chars = ";admin=true;"

    for i in range(0, len(malicious_chars)):

        target_num = starting_byte + i                              # index of the target byte
        target = c[target_num]                                      # original target byte
        m_char = get_replacement_byte(target, malicious_chars[i])   # malicious char to replace the target byte
        b_array[target_num] = int(m_char, 2)                        # update b_array with malicious char

    return bytes(b_array).decode('latin1')

if __name__ == '__main__':

    ciphertext = sanitizer("x" * 19)   # 1 full block plus offset of 3 since sanitized prepend is 29 bytes
    modified_ciphertext = injector(ciphertext)
    check = checker(modified_ciphertext)

    print("\nTest string \";admin=true;\" detected: " + str(check))
