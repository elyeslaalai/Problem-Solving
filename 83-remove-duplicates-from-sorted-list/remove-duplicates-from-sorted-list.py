# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        curr = head

        while curr:

            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next

            curr = curr.next

        return head