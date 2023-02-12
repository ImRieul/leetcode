class Solution:
    def isValid(self, s: str) -> bool:
        box: list = []

        left = ['(', '[', '{']
        right = [')', ']', '}']
        count = 0

        for i in range(len(s)):
            if s[i] in left:
                box.append(right[left.index(s[i])])
            elif s[i] != box[count]:
            # elif s[i] not in right:
                return False
            else:
                count += 1

        return True