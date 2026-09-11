# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        temp = head
        while temp != None:
            l += 1
            temp = temp.next
        target = l - n

        if l == 1 and n == 1:
            return None

        i = 0
        t = head

        if target == 0:
            return head.next

        while i < target - 1:
            t = t.next
            i += 1
        t.next = t.next.next

        return head