# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        im = {val: i for i, val in enumerate(inorder)}

        pi = len(postorder) - 1

        def make(l: int, r: int) -> Optional[TreeNode]:
            nonlocal pi
            if l > r:
                return None

            v = postorder[pi]
            pi -= 1
            root = TreeNode(v)
            i = im[v]
            root.right = make(i + 1, r)
            root.left = make(l, i - 1)
            return root

        return make(0, len(inorder) - 1)