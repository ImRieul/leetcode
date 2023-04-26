# 정수 배열의 숫자가 감소하지 않는 순서로 정렬되어 있을 때, 각 고유 요소가 한 번만 나타나도록 중복된 요소를 제자리에서 제거합니.
# 요소의 상대적 순서는 동일하게 유지해야 합니다. 그런 다음 고유 요소의 개수를 숫자로 반환합니다.
#
# nums의 고유 요소 수를 k라고 가정하고, 이를 허용하려면 다음과 같은 작업을 수행해야 합니다:
#
# nums의 처음 k 요소에 처음에 nums에 있던 순서대로 고유 요소가 포함되도록 배열 nums를 변경합니다.
# nums의 나머지 요소는 nums의 크기만큼 중요하지 않습니다. k를 반환합니다.
#
# 사용자 지정 판사:
# 판사는 다음 코드를 사용하여 솔루션을 테스트합니다:
###############################################################################################
#
# int[] nums = [...]; // Input array(입력 배열)
# int[] expectedNums = [...]; // The expected answer with correct length(올바른 길이의 예상 답입니다)
#
# int k = removeDuplicates(nums); // Calls your implementation(구현을 호출합니다)
#
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#
###############################################################################################
#
# 모든 어설션이 통과하면 솔루션이 승인됩니다.
from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        compare_nums: list = list(set(nums))
        k: int = len(compare_nums)
        compare_nums.sort()
        compare_nums.extend([0 for x in range(len(nums) - len(compare_nums))])

        for i in range(len(nums)):
            nums[i] = compare_nums[i]

        return k
