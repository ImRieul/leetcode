from typing import Optional

from library.node import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        check_list = self.inorder(p, q)
        filter_list = list(filter(lambda x: x == False, check_list))

        return len(filter_list) < 1

    def inorder(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        check_list = []

        if p is not None and q is not None:
            check_list.extend(self.inorder(p.left, q.left))
            check_list.append(p.val == q.val)
            check_list.extend(self.inorder(p.right, q.right))
        else:
            check_list.append(p == q)

        return check_list
