from problem1_3 import repeat_key
from hex2Base64 import Hex2Base64
import binascii


# convert a plaintext string to binary
def text2bin(s):
    bin_string = ""
    for x in s:
        chunk = format(ord(x), 'b').rjust(8, '0')
        bin_string += chunk
    return bin_string


# encrypts plaintext with the given plaintext key
def encrypt_vernam(p_text, k):
    bin_key = text2bin(k)                                           # convert key to binary
    bin_text = text2bin(p_text)                                     # convert plaintext to binary
    xor_string = repeat_key(bin_key, len(bin_text))                 # repeat binary key
    ciphertext = hex(int(bin_text, 2) ^ int(xor_string, 2))[2:]     # encrypt, translate to hex
    return ciphertext


# decrypts hex ciphertext with the given plaintext key
def decrypt_vernam(c_text, k):
    bin_key = text2bin(k)                                           # convert key to binary
    bin_text = Hex2Base64.hex2bin(c_text)                           # convert hex to binary
    xor_string = repeat_key(bin_key, len(bin_text))                 # repeat binary key
    hex_text = hex(int(bin_text, 2) ^ int(xor_string, 2))[2:]       # decrypt with xor cipher
    plaintext = str(binascii.unhexlify(hex_text))[2:-1]             # translate to plaintext
    return plaintext


# Tests the encrypt function using the key, plaintext, and answer provided.
# Returns true if the encrypted plaintext matches the ciphertext provided.
def test_vernam():
    key = "ICE"
    plaintext = "We didn't start the fire, It was always burning, Since the world's been turning, We didn't start th" \
                "e fire, No we didn't light it, But we tried to fight it"
    ciphertext = "1e26652d2a2127643169303128313169372d2c632320312065630c3d6332283065282f32283a366921303b2d2c27246969" \
                 "102c27202069372d2c63322631292d64366921202c2d653d3637272a2b2e6f651e26652d2a212764316930312831316937" \
                 "2d2c632320312065630b2663322c632120272b6e3765252a222137652037696901303d63322c63313b2a202d6331266323" \
                 "20242d3d632c3d"
    print("encryption test: " + str(encrypt_vernam(plaintext, key) == ciphertext))
    print("decryption test: " + str(decrypt_vernam(ciphertext, key) == plaintext))


if __name__ == '__main__':
    test_vernam()
