import re

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(re.findall(r'\w+', s)[-1])