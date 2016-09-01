import math
import re


hex2BinDict = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'a': '1010', 'b': '1011', 'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}

base64Dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
              12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
              23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h',
              34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's',
              45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: '0', 53: '1', 54: '2', 55: '3',
              56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+', 63: '/'}

validHex = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}


class Hex2Base64:

    num_equals = 0  # track how many equals signs are needed for the final conversion

    # convert a hex string to a binary string
    @staticmethod
    def hex2bin(s):
        bin_string = ""
        for d in s.lower():
            bin_string += hex2BinDict[d]
        return bin_string

    # pad a binary string so its length is a multiple of 24
    def pad_bin_string(self, s):
        pad_len = 24 - len(s) % 24
        self.num_equals = int(math.floor(pad_len / 6))
        new_len = 24 * math.ceil((len(s)) / 24)
        return s.ljust(new_len, '0')

    # convert a binary string to a decimal number
    @staticmethod
    def bin2dec(s):
        dec_num = 0
        exp = len(s) - 1
        for d in s:
            if d == '1':
                dec_num += int(math.pow(2, exp))
            exp -= 1
        return dec_num

    # map a decimal number to base64 string
    def map_to_base64(self, n):
        s = str(n)
        b64_string = ""
        start = 0
        end = 6
        while end <= len(s):
            bi_index = s[start:end]
            dec_num = self.bin2dec(bi_index)
            b64_string += base64Dict[dec_num]
            start += 6
            end += 6
        return b64_string

    # change end characters to equals signs to if needed
    def add_equals_signs(self, s):
            b_string = s
            if self.num_equals == 1:
                b_string = re.sub('A$', '=', s)
            elif self.num_equals == 2:
                b_string = re.sub('AA$', '==', s)
            return b_string

    # check if a string is valid hex
    @staticmethod
    def is_valid_hex(s):
        ret_value = True
        for c in s:
            if c not in validHex:
                ret_value = False
                break
        return ret_value

    # converts a hex string h to a base64 string b
    def hex2base64(self, h):
        if len(h) % 2 == 1:
            return "Error: hex string must have even length"
        if not self.is_valid_hex(h):
            return "Error: string is not valid hex"
        b = self.hex2bin(h)
        b = self.pad_bin_string(b)
        b = self.map_to_base64(b)
        b = self.add_equals_signs(b)
        return b

if __name__ == '__main__':
    hex_string = input("Enter a hex string: ")
    converter = Hex2Base64()
    print(converter.hex2base64(hex_string))
