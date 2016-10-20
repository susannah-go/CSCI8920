import string


class BadPaddingError(Exception):
    pass


# returns true if a string has all printable characters, otherwise returns false
def is_printable(s):
    printable = True
    for c in s:
        if c not in string.printable:
            printable = False
            break
    return printable


# returns plaintext (without padding) if p has valid PKCS7 padding, otherwise throws an exception
def valid_padding(p):

    b_array = bytearray(str.encode(p))
    last_byte = b_array[-1]

    if last_byte == 0:
        return False

    for k in range(1, last_byte + 1):
        if b_array[-1] != last_byte:
            # raise BadPaddingError
            return False
        else:
            b_array.pop()

        # s = bytes(b_array).decode('ascii')
        # print(s)
    return True

    # except BadPaddingError:
    #     print("Invalid PKCS7 padding")


def test_case_1():
    b = bytes(bytearray(b'This is a Saturday\x02\x02'))
    return valid_padding(str(b, 'latin1'))


def test_case_2():
    b = bytes(bytearray(b'This is a Saturda\x03\x02\x02'))
    return valid_padding(str(b, 'latin1'))


def test_case_3():
    b = bytes(bytearray(b'This is a Saturda\x03\x02\x01'))
    return valid_padding(str(b, 'latin1'))

if __name__ == '__main__':
    print(test_case_1())
    print(test_case_2())
    print(test_case_3())
