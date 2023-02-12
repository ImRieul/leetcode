# 230204 False
# https://leetcode.com/problems/permutation-in-string/
# Medium

# Solution
# https://leetcode.com/problems/permutation-in-string/solutions/127729/short-permutation-in-a-long-string/?orderBy=hot


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        condition: list = list(s1)

        for i in range(len(s2) - 1):
            if s2[i] in list(s1):
                condition.remove(s2[i])

                if not condition:
                    return True
                elif s2[i+1] not in condition:
                    return False


if __name__ == '__main__':
    s = Solution()

    test1 = 'ab'
    test2 = 'eidbaooo'
    test3 = 'eidboaoo'
    test4 = 'abcd'

    print(s.checkInclusion(test1, test2), 'need True')
    print(s.checkInclusion(test1, test3), 'need False')
    print(s.checkInclusion(test1, test4), 'need True')
