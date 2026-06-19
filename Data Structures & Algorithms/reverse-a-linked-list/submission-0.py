# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = list()
        if head == None:
            return head
        curr = head
        while curr != None:
            result.insert(0, curr.val)
            curr = curr.next
        
        result_list = ListNode(result[0])
        result.pop(0)
        curr = result_list
        for res in result:
            temp = ListNode(res)
            curr.next = temp
            curr = curr.next
        return result_list

        


        