# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        temp = dummy

        while list1 or list2:

            if not list1:
                temp.next = list2
                return dummy.next
            
            elif not list2:
                temp.next = list1
                return dummy.next
            
            else:
                num1 = list1.val
                num2 = list2.val
                if num1 <= num2:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
            
            temp = temp.next
        
        return dummy.next