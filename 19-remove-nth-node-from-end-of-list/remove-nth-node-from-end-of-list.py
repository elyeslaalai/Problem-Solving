# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        if not head:
            return head
        
        temp, length = head, 1
        while temp.next:
            length += 1
            temp = temp.next

        if length == 1 or length == n:
            return head.next
        
        temp, counter = head, 1
        while counter < length - n:
            counter += 1
            temp = temp.next
        
        temp.next = temp.next.next
        return head
        

