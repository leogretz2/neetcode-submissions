# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        triList = []
        # Handle empty input
        if not root:
            return triList
        if not root.left and not root.right:
            triList.append(root.val)
        else:
            triList += self.postorderTraversal(root.left)
            triList += self.postorderTraversal(root.right)
            triList.append(root.val)
        return triList