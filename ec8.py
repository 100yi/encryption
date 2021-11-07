# Cipher name is EC8. This is binary cipher. One character encode by five bits.


_dict_to_ec8 = {
    ' ': '00010',
    'a': '10100',
    'b': '11100',
    'c': '00101',
    'd': '00011',
    'e': '10011',
    'f': '11001',
    'g': '00100',
    'h': '11010',
    'i': '11101',
    'j': '10101',
    'k': '00110',
    'l': '10110',
    'm': '00111',
    'n': '01000',
    'o': '10010',
    'p': '11111',
    'q': '11110',
    'r': '11011',
    's': '01001',
    't': '01111',
    'u': '10111',
    'v': '01010',
    'w': '10001',
    'x': '01011',
    'y': '11000',
    'z': '01110'
}

_dict_to_eng = {
    '00010': ' ',
    '10100': 'a',
    '11100': 'b',
    '00101': 'c',
    '00011': 'd',
    '10011': 'e',
    '11001': 'f',
    '00100': 'g',
    '11010': 'h',
    '11101': 'i',
    '10101': 'j',
    '00110': 'k',
    '10110': 'l',
    '00111': 'm',
    '01000': 'n',
    '10010': 'o',
    '11111': 'p',
    '11110': 'q',
    '11011': 'r',
    '01001': 's',
    '01111': 't',
    '10111': 'u',
    '01010': 'v',
    '10001': 'w',
    '01011': 'x',
    '11000': 'y',
    '01110': 'z',
}


class Ec8:
    def __init__(self, strng):
        self.WTC = strng # WTC => What To Code

    def encode_ec8(self):
        new_strng = ''
        for i in self.WTC:
            if _dict_to_ec8.get(i) != None:
                new_strng += _dict_to_ec8.get(i)
            else:
                new_strng += i
        self.encoded_value = new_strng
        return self.encoded_value

    def decode_ec8(self):
        new_strng = ''
        lst = []
        counter = 0
        for i in self.encoded_value:
            if i != '0' and i != '1':
                lst.append(i)
                continue
            new_strng += i
            counter += 1
            if counter % 5 == 0:
                lst.append(new_strng)
                counter = 0
                new_strng = ''
        new_strng = ''
        for i in lst:
            if _dict_to_eng.get(i) != None:
                new_strng = new_strng + _dict_to_eng.get(i)
            else:
                new_strng = new_strng + i
        self.decoded_value = new_strng
        return self.decoded_value

    def get_value(self):
        try:
            return f'WTC: {self.WTC}, Encoded: {self.encoded_value}, Decoded: {self.decoded_value}'
        except:
            return 'Use .encode_ec8() and .decode_ec8() later use .value'

    value = property(fget=get_value)
