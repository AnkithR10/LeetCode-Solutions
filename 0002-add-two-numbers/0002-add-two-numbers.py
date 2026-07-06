# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Extract values, default to 0 if list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Append new node
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to next nodes if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next