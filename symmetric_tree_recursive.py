# 23.72%
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if (left == None) and (right == None):
            return True
        if (left == None) or (right == None):
            return False
        if left.val == right.val:
            outpair = self.isMirror(left.left, right.right)
            inpair = self.isMirror(left.right, right.left)
            if outpair and inpair:
                return True
        return False