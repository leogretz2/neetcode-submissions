# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subSig = self.signature(subRoot)

        seen = set()
        def collect(node):
            if not node:
                return ('#',)
            leftSig = collect(node.left)
            rightSig = collect(node.right)
            sig = (node.val, leftSig, rightSig)
            seen.add(sig)
            return sig

        collect(root)
        return subSig in seen

    def signature(self, node):
        if not node:
            return ("#",)
        return (node.val, self.signature(node.left), self.signature(node.right))
        