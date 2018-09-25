# 48.69%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # find the next node
        nxt_node = node.next
        
        # replace node self as the next node
        node.val = nxt_node.val
        node.next = nxt_node.next