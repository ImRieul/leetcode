from typing import List, Optional

from library.node import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorder(root)

    def inorder(self, root: Optional[TreeNode]):
        traversal = []
        if root is not None:
            traversal.extend(self.inorder(root.left))
            traversal.append(root.val)
            traversal.extend(self.inorder(root.right))

        return traversal