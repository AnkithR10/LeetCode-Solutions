# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        slow = head
        fast = head
        
        # Move fast by 2 steps and slow by 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # When fast reaches the end, slow is at the middle
        return slow