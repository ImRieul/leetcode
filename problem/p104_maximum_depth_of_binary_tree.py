from typing import Optional, List

from library.node import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth_check = []
        #
        # depth: int = 0
        #
        # while root is not None:
        #     depth += 1
        #     if root.left is not None:
        #         root = root.left
        #     elif root.right is not None:
        #         root = root.right
        #     else:
        #         depth_check.append(depth)
        #         depth = 0

        return self.deep(root, 0)


    def deep(self, root: Optional[TreeNode], dept: int) -> int:
        if root is not None:
            dept += 1
            left = self.deep(root.left, dept)
            right = self.deep(root.right, dept)

            dept = max(dept, left, right)

        return dept
