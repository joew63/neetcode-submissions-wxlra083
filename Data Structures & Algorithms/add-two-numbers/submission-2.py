class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        extra = 0

        result = None
        curr_result = None

        while(curr_l1 != None or curr_l2 != None or extra > 0):
            c1, c2 = 0, 0
            if curr_l1 != None:
                c1 = curr_l1.val
            if curr_l2 != None:
                c2 = curr_l2.val
            
            added = c1 + c2 + extra
            extra = added // 10
            val = added % 10
            
            if result is None:
                result = ListNode(val)
                curr_result = result
            else:
                curr_result.next = ListNode(val)
                curr_result = curr_result.next
            
            if curr_l1 != None:
                curr_l1 = curr_l1.next
            if curr_l2 != None:
                curr_l2 = curr_l2.next
                
        return result