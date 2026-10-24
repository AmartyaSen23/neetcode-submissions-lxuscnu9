# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 0
        if root==p:
            return root
        if root==q:
            return root
        a = self.lowestCommonAncestor(root.left,p,q)
        b = self.lowestCommonAncestor(root.right,p,q)
        if (a and not b):
            return a
        elif (b and not a):
            return b
        elif (a and b):
            return root
        else:
            return None