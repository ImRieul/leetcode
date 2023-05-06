from typing import Optional
from library.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        updated_node = ListNode(head.val)
        first_node = updated_node

        while head:
            if head.next and head.val != head.next.val:
                updated_node.next = ListNode(head.next.val)
                updated_node = updated_node.next

            head = head.next

        return first_node


if __name__ == '__main__':
    s = Solution()
    node = ListNode().from_list([1, 2, 3, 3])

    after_node = s.deleteDuplicates(node)
    print(after_node.to_list())