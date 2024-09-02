# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head and head.val == val:
            head = head.next

        newHead = head

        if not newHead:
            return None

        temp = newHead
        
        while temp and temp.next:
            while temp and temp.next and temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next

        return newHead
