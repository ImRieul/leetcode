# https://leetcode.com/problems/fruit-into-baskets/
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
#
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
#
# - You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# - Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
from typing import List


# TODO dict, list에 저장을 해서 시간이 많이 늦어져 Time Limit Exceeded가 떴다.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        bag1 = []
        bag2 = []

        for index in range(len(fruits)):
            for fruit in fruits[index:]:
                if fruit in bag1 or len(bag1) == 0:
                    bag1.append(fruit)
                elif fruit in bag2 or len(bag2) == 0:
                    bag2.append(fruit)
                else:
                    break

            count[index] = len(bag1) + len(bag2)
            bag1 = []
            bag2 = []

        return max(count.values())

# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.

# Example 2:
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].

# Example 3:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

# Example 4:
# Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can pick from trees [1,2,1,1,2].
# If we had started at the first tree or the eighth tree, we would only pick from trees [3,3].

# Example 5:
# Input: fruits = [1,0,1,4,1,4,1,2,3]
# Output: 5
# Explanation: We can pick from trees [1,4,1,4,1,2,3].
# If we had started at the first tree, we would only pick from trees [1,0,1].


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         # Maximum number of fruits we can pick
#         # 우리가 고를 수 있는 최대 과일 수
#         max_picked = 0
#
#         # Iterate over all subarrays: left index left, right index right.
#         # 왼쪽 인덱스 왼쪽, 오른쪽 인덱스 오른쪽 등 모든 하위 배열에 대해 반복합니다.
#         for left in range(len(fruits)):
#             for right in range(left, len(fruits)):
#                 # Use a set to count the type of fruits.
#                 # 과일의 종류를 세는데 한 세트를 사용하세요.
#                 basket = set()
#
#                 # Iterate over the current subarray (left, right).
#                 # 현재 하위 배열(왼쪽, 오른dd쪽)에 대해 반복합니다.
#                 for current_index in range(left, right + 1):
#                     basket.add(fruits[current_index])
#
#                 # If the number of types of fruits in this subarray (types of fruits)
#                 # 이 하위 배열의 과일 종류 수(과일 종류)
#                 # is no larger than 2, this is a valid subarray, update 'max_picked'.
#                 # 2보다 크지 않습니다. 이것은 유효한 하위 배열입니다. 'max_delay' 업데이트.
#                 if len(basket) <= 2:
#                     max_picked = max(max_picked, right - left + 1)
#
#         # Return 'max_picked' as the maximum length (maximum number of fruits we can pick).
#         return max_picked


if __name__ == '__main__':
    fruits = [
        [1,2,1],
        [0,1,2,2],
        [1,2,3,2,2],
        [3,3,3,1,2,1,1,2,3,3,4],
        [1,0,1,4,1,4,1,2,3]
    ]

    ok = [
        3,
        3,
        4,
        5,
        5
    ]

    for i in range(len(fruits)):
        print(Solution().totalFruit(fruits[i]) == ok[i])

# Constraints:
# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length

