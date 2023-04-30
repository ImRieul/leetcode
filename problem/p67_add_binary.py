class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_10 = int(a, 2) + int(b, 2)
        return format(num_10, 'b')