# 91%
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        t = [head.val]
        while head and head.next:
            t.append(head.next.val)
            head = head.next
        
        mid = len(t)/2
        if len(t)%2 == 0:  
            return t[:mid][::-1] == t[mid:]
        else:
            return t[:mid+1][::-1] == t[mid:]