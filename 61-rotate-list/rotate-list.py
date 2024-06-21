# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        # edge cases:
        if not head or not head.next:
            return head
        
        if not k or k == 0:
            return head
        
        tail, length = head, 1
        while tail.next:
            length += 1
            tail = tail.next
        tail.next = head
    
        temp, k = head, k % length
        for _ in range(length - k - 1):
            temp = temp.next
        answer = temp.next
        temp.next = None

        return answer


        

        

        
