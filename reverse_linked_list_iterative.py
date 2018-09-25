# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # iteration
        prev_head = None        
        while head:
            #head.next, head.next.next = prev_head, head.next
            curr = head
            head =  head.next
            curr.next = prev_head
            prev_head = curr          
        return prev_head