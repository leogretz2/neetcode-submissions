# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.assessTriNode(root)

    def assessTriNode(self, top: Optional[TreeNode]) -> List[int]:
        triList = []
        # Handle empty input
        if not top:
            return triList
        if not top.left and not top.right:
            triList.append(top.val)
        else:
            triList += self.assessTriNode(top.left)
            triList += self.assessTriNode(top.right)
            triList.append(top.val)
        return triList

        # triList = []
        # triList += [top.value, top.left.value, top.right.value]
        