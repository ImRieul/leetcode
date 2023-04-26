

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()

        for i in range(len(nums)):
            if nums[i] == target:
                return i


# 신박한 풀이
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         is_found = False
#
#         for index, item in enumerate(nums):
#             if item >= target:
#                 return index
#
#         return len(nums)