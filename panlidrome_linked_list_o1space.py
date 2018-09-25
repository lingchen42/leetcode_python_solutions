# O(1) space complexity, O(n) time
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
        # find mid
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None   
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        slow = prev
        
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True