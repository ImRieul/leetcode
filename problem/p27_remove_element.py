from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:

        val_count: list = len(list(filter(lambda x: x == val, nums)))

        for i in range(val_count):
            nums.remove(val)

        return len(nums)




# 신박한 풀이 (속도를 높이는 방법)
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)