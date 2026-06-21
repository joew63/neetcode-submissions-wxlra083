# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next
        if count - n == 0:
            return head.next
        
        new_count = 0
        curr = head
        while curr != None and curr.next != None:
            new_count += 1
            if new_count == count - n:
                curr.next = curr.next.next
            curr = curr.next

        return head
        