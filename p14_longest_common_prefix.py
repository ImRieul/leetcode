# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # list 안에 중복되는 단어를 찾기.

        strs.sort(key=len)      # 가장 적은 단어를 기준으로 for문을 돌린다.
        result: str = ''

        for i in range(len(strs[0])):               # 기준 단어 for
            for j in strs:                      # 검사할 단어 for
                if strs[0][i] != j[i]:
                    return result

            result += strs[0][i]

        return result
