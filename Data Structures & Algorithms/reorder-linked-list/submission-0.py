# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        curr1 = head
        while second != None:
            temp1 = curr1.next
            curr1.next = second
            second = second.next
            curr1.next.next = temp1
            curr1 = temp1