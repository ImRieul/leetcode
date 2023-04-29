from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str: str = ''.join(list(map(str, digits)))
        num: int = int(num_str) + 1

        return list(map(int, str(num)))
