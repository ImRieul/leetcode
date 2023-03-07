class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        division = len(s) // 2
        return s[:division] == s[::-1][:division]
