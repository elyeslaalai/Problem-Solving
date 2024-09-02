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
        
        mid = head
        i = 0
        end = length / 2 if length % 2 == 0 else length / 2 + 1

        for _ in range(end):
            mid = mid.next
            i += 1
        
        prev, curr = None, head
        for _ in range(end):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        if length % 2 == 1:
            prev = prev.next
            end -= 1
        
        for _ in range(end):
            if prev.val != mid.val:
                return False
            prev = prev.next
            mid = mid.next

        return True

    
