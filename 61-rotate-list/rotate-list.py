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
        
        # edge cases
        if not head or not head.next or k == 0:
            return head

        length = 0
        temp = head

        while temp:
            length += 1
            tail = temp
            temp = temp.next
        
        rotations = k % length

        if rotations == 0:
            return head
        
        dummyHead = ListNode(-1)

        temp, i = head, 1
        while i < length - rotations:
            temp = temp.next
            i += 1

        prev = temp
        curr = temp.next


        dummyHead.next = curr
        tail.next = head
        prev.next = None

        return dummyHead.next 
        

        

        

        
