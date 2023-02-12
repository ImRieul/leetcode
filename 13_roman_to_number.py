class Solution:
    def __init__(self):
        self.minor_dic = {
            'IV': '4',
            'IX': '9',
            'XL': '40',
            'XC': '90',
            'CD': '400',
            'CM': '900'
        }

        self.major_dic = {
            'I': '1',
            'V': '5',
            'X': '10',
            'L': '50',
            'C': '100',
            'D': '500',
            'M': '1000',
        }

        self.str: str = ""

    def replace_dic(self, dic: dict):
        for k, v in dic.items():
            self.str = self.str.replace(k, '-' + v)

    def add_str(self) -> int:
        result: int = 0
        str_list: list = list(map(int, self.str.split('-')[1:]))
        for i in str_list:
            result += i
        return result

    def roman_to_int(self, s: str) -> int:
        self.str = s
        self.replace_dic(self.minor_dic)
        self.replace_dic(self.major_dic)
        return self.add_str()


if __name__ == '__main__':
    s = Solution()

    test1 = 'III'
    test2 = 'LVIII'
    test3 = 'MCMXCIV'

    value1 = s.roman_to_int(test1)
    value2 = s.roman_to_int(test2)
    value3 = s.roman_to_int(test3)

    print(3, 'value1=' + str(value1), 3 == value1)
    print(58, 'value2=' + str(value2), 58 == value2)
    print(1994, 'value3=' + str(value3), 1994 == value3)
