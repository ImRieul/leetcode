class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        result = ''

        for i in s:
            if i in dic.keys():
                result += dic[i]
            elif result != '' and result[-1] == i:
                result = result[:-1]
            else:
                return False

        return result == ''
