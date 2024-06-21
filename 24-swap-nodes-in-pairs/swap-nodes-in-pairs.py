# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        dummyHead = ListNode(-1)

        prev = dummyHead
        curr = head

        while curr and curr.next:

            nextPair = curr.next.next
            nextNode = curr.next

            prev.next = nextNode
            nextNode.next = curr
            curr.next = nextPair

            prev = curr
            curr = curr.next
        
        return dummyHead.next
        