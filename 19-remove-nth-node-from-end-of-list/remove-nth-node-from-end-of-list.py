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
        
        tail, length = head, 1
        while tail.next:
            tail = tail.next
            length += 1
        
        if n == length:
            return head.next
        
        temp, i = head, 1

        while i < length - n:
            temp = temp.next
            i += 1
        
        print(temp.val)

        temp.next = temp.next.next
        return head




