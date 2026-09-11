# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None

        head = ListNode()
        t = head
        t1 = list1
        t2 = list2

        while t1 != None and t2 != None:
            if t1.val > t2.val:
                t.val = t2.val
                t2 = t2.next
            else:
                t.val = t1.val
                t1 = t1.next
            t.next = ListNode()
            t = t.next
        
        while t1 != None:
            t.val = t1.val
            t1 = t1.next
            if t1 != None:
                t.next = ListNode()
                t = t.next

        while t2 != None:
            t.val = t2.val
            t2 = t2.next
            if t2 != None:
                t.next = ListNode()
                t = t.next

        return head