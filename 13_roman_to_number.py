class Solution:
    def __init__(self):
        minor_dic = {
            'IV': ',4',
            'XL': ',40',
            'XC': ',90',
            'CD': ',400',
            'CM': ',900'
        }

        major_dic = {
            'I': ',1',
            'V': ',5',
            'X': ',10',
            'L': ',50',
            'C': ',100',
            'D': ',500',
            'M': ',1000',
        }

            # I: 1,
            # IV: 4,
            # V: 5,
            # IX: 9,
            # X: 10,
            # XL: 40,
            # L: 50,
            # XC: 90,
            # C: 100,
            # CD: 400,
            # D: 500,
            # CM: 900,
            # M: 1000,

        self.result: int = 0
        self.str: str = ""

    def minor(self, value):
        pass

    def conversion(self):
        if self.result in self.dic.keys():
            self.result = 1

    def roman_to_int(self, s: str) -> int:
        self.str = s
