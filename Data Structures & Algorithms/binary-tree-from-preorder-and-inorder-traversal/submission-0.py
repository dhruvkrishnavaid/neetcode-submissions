# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        im = {val: i for i, val in enumerate(inorder)}

        pi = 0

        def make(l: int, r: int) -> Optional[TreeNode]:
            nonlocal pi
            if l > r:
                return None

            v = preorder[pi]
            pi += 1
            root = TreeNode(v)
            i = im[v]
            root.left = make(l, i - 1)
            root.right = make(i + 1, r)
            return root

        return make(0, len(inorder) - 1)