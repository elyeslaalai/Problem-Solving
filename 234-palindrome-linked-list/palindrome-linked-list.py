import math

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        
        temp = head
        stack = []

        for _ in range(length / 2):
            stack.append(temp.val)
            temp = temp.next
        
        start = length / 2
        if length % 2 == 1:
            temp = temp.next
            start += 1
        
        for _ in range(start, length):
            popped = stack.pop()
            if popped != temp.val:
                return False
            temp = temp.next

        return True
    
