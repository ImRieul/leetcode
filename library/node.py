from typing import List


class ListNode:
    def __init__(self, val = 0, next_node = None):
        self.val = val
        self.next: ListNode = next_node


    def to_list(self) ->  List:
        return_list = []

        while self.next:
            return_list.append(self.val)
            self = self.next

        return_list.append(self.val)

        return return_list

    def from_list(self, val_list):
        node_left = None
        node_right = None

        for val in val_list[::-1]:
            node_left = ListNode(val)
            if node_right:
                node_left.next = node_right

            node_right = node_left

        return node_left

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == '__main__':
    # node2 = ListNode(2)
    # node1 = ListNode(1, node2)
    # node0 = ListNode(0, node1)
    # print(node0.to_list())

    node1 = ListNode().from_list([1, 3, 2, 3])

    while node1:
        print(node1.val)
        node1 = node1.next


