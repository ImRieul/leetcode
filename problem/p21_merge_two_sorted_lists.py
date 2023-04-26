# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2

        return dummy.next


# 인상에 남았던 풀이 방법. while 문을 사용하지 않고 재귀를 사용해서 풀었다.
class Solution_remember:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1, h2 = list1, list2
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.val < h2.val:
            return ListNode(h1.val, self.mergeTwoLists(h1.next, h2))
        else:
            return ListNode(h2.val, self.mergeTwoLists(h1, h2.next))