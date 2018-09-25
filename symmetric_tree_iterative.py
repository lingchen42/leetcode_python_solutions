# 65.77% iterative using python implemented queue
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
        
        q = [[root, root]]
        while len(q):
            # check if equal
            t1, t2 = q.pop(0)
            if (t1==None) and (t2==None): continue
            if (t1==None) or (t2==None): return False
            if t1.val != t2.val:
                return False
            else:
                q.insert(0, [t1.left, t2.right])
                q.insert(0, [t1.right, t2.left])
        return True        